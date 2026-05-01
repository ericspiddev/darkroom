from abc import ABCMeta, abstractmethod
class IDarkRoomOsOperations(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'file_exists') and
                callable(subclass.file_exists) and
                hasattr(subclass, 'get_current_directory') and
                callable(get_current_directory) and
                hasattr(subclass, 'join_paths') and
                callable(join_paths) and
                hasattr(subclass, 'open_file') and
                callable(open_file) or
                NotImplemented)

    @abstractmethod
    def file_exists(self, path):
        raise NotImplementedError

    @abstractmethod
    def get_current_directory(self):
        raise NotImplementedError

    @abstractmethod
    def join_paths(self, path_one, path_two):
        raise NotImplementedError

    @abstractmethod
    def str_join_paths(self, path_one, path_two):
        raise NotImplementedError

    @abstractmethod
    def open_file(self, file_path, modes):
        raise NotImplementedError

    @abstractmethod
    def close_file(self, file_object):
        raise NotImplementedError
