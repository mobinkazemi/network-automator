import asyncio
import time
import paramiko

from switches.model import Switch


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
