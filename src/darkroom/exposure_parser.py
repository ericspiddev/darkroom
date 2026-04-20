import yaml

class ExposureParser:
    def __init__(self, os_ops):
        self.exposure_yaml = []
        self.os_ops = os_ops

    def is_yaml_loaded(self):
        return len(self.exposure_yaml) != 0

    def parse_exposure(self, command, directory):
        self.load_exposure_file(directory)

    def load_exposure_file(self, directory):
        exposure_path = self.os_ops.join_paths(directory, ".exposure.yml")
        exposure_file = self.os_ops.load_readonly_file(exposure_path)
        if not exposure_file:
            print(f'Load exposure file failed')
            return
        self.exposure_yaml = yaml.safe_load(exposure_file)
        print(f"Exposure yaml is {self.exposure_yaml}")
        self.os_ops.close_file(exposure_file)
