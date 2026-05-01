from interfaces.os.darkroom_os_operations import IDarkRoomOsOperations

class OsOperations():
    def __init__(self, os_ops: IDarkRoomOsOperations):
        self.os_ops = os_ops

    def file_exists(self, file_path):
        return self.os_ops.file_exists(file_path)

    def get_current_directory(self):
        return self.os_ops.get_current_directory()

    def join_paths(self, path_one, path_two):
        return self.os_ops.join_paths(path_one, path_two)

    def str_join_paths(self, path_one, path_two):
        return self.os_ops.str_join_paths(path_one,path_two)

    def load_readonly_file(self, file_path):
        return self.os_ops.open_file(file_path, 'r')

    def open_file(self, file_path, modes):
        if self.file_exists(file_path):
            return self.os_ops.open_file(file_path, modes)
        else:
            print(f'Error: could not open file at {file_path} with modes {modes}')
            return None

    def close_file(self, file):
        self.os_ops.close_file(file)
