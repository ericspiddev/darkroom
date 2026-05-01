from darkroom.interfaces.developments.darkroom_development import IDarkRoomDevelopment
from darkroom.interfaces.transports.darkroom_ssh import IDarkRoomSSHTransport
from darkroom.interfaces.transports.darkroom_transports import DarkRoomTransports

class SSHDevelopment(IDarkRoomDevelopment):

    def __init__(self, ssh_ops: IDarkRoomSSHTransport, os_ops: IDarkRoomOsOperations):
        self.transport_id = DarkRoomTransports.SSH.value
        self.ssh_ops = ssh_ops
        self.os_ops = os_ops

    def setup(self, image_data, transport_data):
        for server in transport_data.remote_servers:
            self._append_dest_path(image_data, server.prefix_path)
            self.ssh_ops.ssh_setup(image_data, server)

    def _append_dest_path(self, images, prefix_path):
        for image in images:
           image.dest_path = self.os_ops.str_join_paths(prefix_path, image.dest_path)

    def teardown(self):
        self.ssh_ops.ssh_teardown()

    def pull_images(self, pull_path):
        self.ssh_ops.ssh_pull(pull_path)

    def push_images(self):
        self.ssh_ops.ssh_put()




