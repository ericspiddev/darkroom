import abc
from darkroom.interfaces.transports.darkroom_transports import DarkRoomTransports
from darkroom.interfaces.transports.darkroom_ssh import SSHTransportData, SSHServer
from darkroom.project import DarkRoomProject
from darkroom.data.darkroom_data import DarkRoomDataClass

class IDarkRoomParser(metaclass=abc.ABCMeta):

    def __init():
        self.parsed_data = None
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'parse_exposrue') and
                callable(subclass.parse_exposure) or
                NotImplemented)

    @abc.abstractmethod
    def parse_exposure(self, exposure_file, operation):
        raise NotImplementedError

    def can_parse(self):
        if self.parsed_data == None:
            raise Error("Cannot parse with empty parse data object")

    def get_element(self, element, data=None):
        if not data:
            data = self.parsed_data
            if not data:
                raise ValueError(f"NULL dataset will not look for key! {element}")
        if data[element] == None:
            raise ValueError(f"Cannot find key {element} in dataset {self.parsed_data}")
        return data[element]

    def parse_projects(self, os_ops):
        try:
            self.can_parse()
        except e:
            print(e)
            return False
        projects = []
        for project in self.get_element('projects'):
            project_object = DarkRoomProject(project, os_ops)
            parsed_transports = []
            for transport in project_object.transports:
                transport.data = self.parse_transport(transport.transport_type, transport.data)
                parsed_transports.append(transport)

            project_object.transports = parsed_transports
            projects.append(project_object)

        return projects

    def parse_transport(self, transport, data) -> DarkRoomDataClass:
        try:
            self.can_parse()
        except e:
            print(e)
            return None
        if transport == DarkRoomTransports.SSH.value:
            return self.parse_ssh(data)

    def parse_ssh(self, transport_data):
        try:
            self.can_parse()
        except e:
            print(e)
            return False
        return SSHTransportData(transport_data)
