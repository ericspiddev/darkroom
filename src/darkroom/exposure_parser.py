from dataclasses import dataclass
from darkroom.interfaces.os.darkroom_os_operations import IDarkRoomOsOperations
from darkroom.interfaces.transports.darkroom_transports import DarkRoomTransports
from darkroom.data.darkroom_data import DarkRoomDataClass
from darkroom.project import DarkRoomProject

@dataclass
class ParsedData():
    projects : list[DarkRoomProject]

class ExposureParser():
    def __init__(self, parser: IDarkRoomParser, os_ops: IDarkRoomOsOperations):
        self.parser = parser
        self.parsed_exposure = []
        self.exposure_is_parsed = False
        self.os_ops = os_ops

    def parse_exposure(self, directory, transport) -> ParsedData:
        self.exposure_is_parsed = False
        exposure_file = self.load_exposure_file(directory)
        if not exposure_file:
            print(f'Parse Exposure: failed to load exposure file from {directory}')

        if not self.parser.parse_exposure(exposure_file):
            print(f'Parse Exposure: failed to parse exposure file from {directory}')

        projects = self.parser.parse_projects(self.os_ops)
        if not projects:
            print(f'Parse Exposure: failed to parse projects from exposure file in {directory}')

        return projects[0] # Let's start just returning 1 project for now


    def load_exposure_file(self, directory):
        exposure_path = self.os_ops.join_paths(directory, ".exposure.yml")
        exposure_file = self.os_ops.load_readonly_file(exposure_path)
        return exposure_file
