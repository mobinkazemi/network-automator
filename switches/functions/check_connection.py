import paramiko

from switches.model import Switch


def check_ssh_connection(data: Switch) -> bool:
    try:
        client = paramiko.Transport((data["ip"], 22))
        client.connect(username=data["username"], password=data["password"])
        client.close()
        return True
    except Exception as e:
        print(e)
        return False
