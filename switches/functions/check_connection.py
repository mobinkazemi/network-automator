import asyncio
import time
import paramiko
from switches.model import Switch
from hardening.hardeningCheckList import hardeningCheckList


async def check_ssh_connection(data: Switch, ttl: int) -> bool:
    try:
        return await asyncio.wait_for(_connect_with_timeout(data), timeout=ttl)
    except asyncio.TimeoutError:
        return {"id": data["id"], "result": False}


async def _connect_with_timeout(data: Switch) -> bool:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, _connect_ssh, data)
    return result


def _connect_ssh(data: Switch, second_try: bool = False) -> bool:
    try:
        client = paramiko.Transport((data["ip"], 22))
        client.connect(
            username=data["username"],
            password=data["password"],
        )

        client.close()

        return {"id": data["id"], "result": True}
    except Exception as e:
        return {"id": data["id"], "result": False}


def run_cisco_command(host, username, password, command):
    try:

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_client.connect(
            hostname=host,
            username=username,
            password=password,
            allow_agent=False,
            look_for_keys=False,
            timeout=10,
        )

        ssh_client.get_transport().set_keepalive(30)

        channel = ssh_client.invoke_shell()
        time.sleep(1)

        if channel.recv_ready():
            channel.recv(65535)

        print(f"Running command: {command}")
        channel.send(command + "\n")
        time.sleep(1)
        output = ""
        while True:
            if channel.recv_ready():
                output = channel.recv(65535).decode("utf-8")
            else:
                break
            time.sleep(1)
        channel.close()
        ssh_client.close()
        print(output)
        return output

    except paramiko.ssh_exception.SSHException as ssh_err:
        return {
            "message": "مشکلی در برقراری ارتباط به وجود آمده است",
        }
    except EOFError:
        return {
            "message": "ارتباط قطع شد",
        }
    except Exception as e:
        return {
            "message": "عدم توانایی در اتصال",
        }


def run_multiple_commands_separately(host, username, password):
    commandsOutput = []
    for audit in hardeningCheckList:
        commandsOutput.append(
            run_cisco_command(host, username, password, audit["command"])
        )
    return commandsOutput
