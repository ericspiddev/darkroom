from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from data.darkroom_data import DarkRoomDataClass
from project import DarkRoomProjectTransport

@dataclass
class SSHServer(DarkRoomDataClass):
    def __init__(self, raw_data):
        super().__init__(raw_data)
    name: str = field(init=False)
    hostname: str = field(init=False)
    username: str = field(init=False)
    prefix_path: str = field(init=False)

@dataclass
class SSHTransportData(DarkRoomDataClass):
    def __init__(self, raw_data):
        servers = []
        for server in raw_data['remote_servers']:
            servers.append(SSHServer(server))
        self.remote_servers = servers
    remote_servers: list[SSHServer] = field(init=False)

    def get_extra_path(index=0):
        if len(remote_servers) > index:
            return self.remote_servers[index].prefix_path

class IDarkRoomSSHTransport(metaclass=ABCMeta):

    @abstractmethod
    def ssh_setup():
        raise NotImplementedError

    @abstractmethod
    def ssh_put():
        raise NotImplementedError

    @abstractmethod
    def ssh_pull():
        raise NotImplementedError

    @abstractmethod
    def ssh_teardown():
        raise NotImplementedError


