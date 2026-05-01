from interfaces.os.darkroom_os_operations import IDarkRoomOsOperations
from pathlib import Path
class PathlibOsOperations(IDarkRoomOsOperations):
    def file_exists(self, file_path):
        return Path(file_path).exists()

    def get_current_directory(self):
        return Path.cwd()

    def join_paths(self, path_one, path_two):
        return Path(path_one).joinpath(path_two)

    def str_join_paths(self, path_one, path_two):
        return str(self.join_paths(path_one, path_two))

    def open_file(self, file_path, modes):
        return open(file_path, modes)

    def close_file(self, file):
        return file.close()

