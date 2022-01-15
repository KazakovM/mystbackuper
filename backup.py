import paramiko
import yaml
from datetime import datetime
from scp import SCPClient


def copy_folder(name, ip, username, password):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip, "22", username, password)
        scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=3.0)
    except Exception as e:
        print(f'Failed to initiate ssh connection for {name}: {e}')

    try:
        local_path = name + "_backup_" + datetime.today().strftime('%Y-%m-%d-%HH-%MM')
        remote_path = f"/var/lib/mysterium-node/keystore"
        scpclient.get(remote_path, local_path, True)
    except Exception as e:
        print(f'Failed to copy backup files for {name}: {e}')

def main():
    try:
        with open(r'config.yaml') as config_file:
            configs = yaml.load(config_file, Loader=yaml.FullLoader)
            servers = configs["servers"]
            for server in servers:
                copy_folder(server["name"], server["ip"], server["username"], server["password"])
    except Exception as e:
        print(f'Exception occured: {e}')

if __name__ == '__main__':
    main()
