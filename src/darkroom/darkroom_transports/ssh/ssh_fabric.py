from fabric import Connection
from darkroom.interfaces.transports.darkroom_ssh import IDarkRoomSSHTransport

class SSHFabric(IDarkRoomSSHTransport):
    def __init__(self):
        self.connected = False

    def _is_connected(data):
        return self.connected

    def ssh_setup(self, image_data, ssh_data):
        self.images = image_data
        self._setup_ssh_conn(ssh_data)
        if self.ssh_conn:
            self.connected = True

    def _setup_ssh_conn(self, ssh_data):
        self.ssh_conn = Connection(ssh_data.hostname, ssh_data.username)
        try:
            self.ssh_conn.open()
        except Exception as e:
            self.ssh_conn = None
            raise Exception(f"Unable to open connection at host {ssh_data.hostname} with user {ssh_data.username} with error {e}")

    def ssh_put(self):
        if not self._is_connected:
            raise Exception("Error not connected to SSH host")

        for image in self.images:
            print(f"put image {image.source_path} to {image.dest_path}")
            self.ssh_conn.put(image.source_path, remote=image.dest_path)

    def ssh_pull(self, pull_path):
        if not self._is_connected:
            print("Error not connected to SSH host")

        for image in self.images:
            print(f"Pull image {image.dest_path} to {pull_path}")
            self.ssh_conn.get(image.dest_path, local=pull_path)

    def ssh_teardown(self):
        if self.ssh_conn:
            self.ssh_conn.close()
            self.ssh_conn = None
            self.connected = False
