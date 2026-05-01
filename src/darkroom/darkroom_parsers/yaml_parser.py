from yaml import safe_load, YAMLError
from interfaces.parser.darkroom_parser import IDarkRoomParser

class YamlExposureParser(IDarkRoomParser):
    def parse_exposure(self, exposure_file):
        yaml_exposure = None
        try:
            yaml_exposure = safe_load(exposure_file)
        except YAMLError as ye:
            print(f"YamlExposureParser: Failed to parse YAML exposure file with error: {ye}")
            return False
        self.parsed_data = yaml_exposure
        return True


    def parse_common_exposure():
        pass

    def parse_operation_exposure(operation):
        pass

    def parse_ssh_exposure():
        pass
