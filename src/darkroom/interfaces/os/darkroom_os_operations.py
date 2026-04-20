import abc
class IDarkRoomOsOperations(metaclass=abc.ABCMeta):
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

    @abc.abstractmethod
    def file_exists(self, path):
        raise NotImplementedError

    @abc.abstractmethod
    def get_current_directory(self):
        raise NotImplementedError

    @abc.abstractmethod
    def join_paths(self, path_one, path_two):
        raise NotImplementedError

    @abc.abstractmethod
    def open_file(self, file_path, modes):
        raise NotImplementedError

    @abc.abstractmethod
    def close_file(self, file_object):
        raise NotImplementedError
