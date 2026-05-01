from abc import ABCMeta, abstractmethod
from enum import Enum

class IDarkRoomDevelopment(metaclass=ABCMeta):
    @abstractmethod
    def setup():
        raise NotImplementedError

    @abstractmethod
    def pull_images():
        raise NotImplementedError

    @abstractmethod
    def push_images():
        raise NotImplementedError

    @abstractmethod
    def teardown():
        raise NotImplementedError
