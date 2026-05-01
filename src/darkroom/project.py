from dataclasses import dataclass, field
from data.darkroom_data import DarkRoomDataClass
from abc import abstractmethod
from interfaces.transports.darkroom_transports import DarkRoomTransports
@dataclass
class DarkRoomProjectImage():
    source_path : str
    dest_path : str

@dataclass
class DarkRoomProjectBuildDir(DarkRoomDataClass):
    path: str
    images: list[DarkRoomProjectImage]
    def __init__(self, raw_data):
        super().__init__(raw_data)

@dataclass
class DarkRoomProjectTransport(DarkRoomDataClass):
    transport_type: str
    data: any
    def __init__(self, key, raw_data):
        self.transport_type = key
        self.data = raw_data

    @abstractmethod
    def get_extra_path():
        raise NotImplementedError

@dataclass
class DarkRoomProject(DarkRoomDataClass):
    name: str
    project_path: str
    pull_path: str
    build_dirs: list[DarkRoomProjectBuildDir]
    transports: list[DarkRoomProjectTransport]

    def __init__(self, raw_data, os_ops: IDarkRoomOsOperations):
        super().__init__(raw_data)
        self.os_ops = os_ops

        data = self.transports
        self.transports = []
        for transport in data:
            self.transports.append(DarkRoomProjectTransport(transport, data[transport], ))

        data = self.build_dirs
        self.build_dirs = []
        for build in data:
            build_dir = DarkRoomProjectBuildDir(build)
            build_dir.images = self.create_build_images(build_dir.path, build_dir.images)
            self.build_dirs.append(build_dir)

    def create_build_images(self, build_dir, image_data):
        images = []
        for image in image_data:
           build_dir_path = self.os_ops.str_join_paths(self.project_path, build_dir)
           source = self.os_ops.str_join_paths(build_dir_path, image['source'])
           images.append(DarkRoomProjectImage(source, image['dest']))
        return images
