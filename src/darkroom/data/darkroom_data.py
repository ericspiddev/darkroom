from dataclasses import dataclass, fields, field
from abc import abstractmethod

@dataclass
class DarkRoomDataClass():

    def __init__(self, raw_data: dict):
        self.raw_data = raw_data
        self.assign_from_raw_data()

    def assign_from_raw_data(self):
        for field in fields(self):
            #print(f"Field is {field} raw data is {self.raw_data}")
            if not self.raw_data[field.name]:
                 raise KeyError(f"Missing field {field.name} for dataclass instantiation")
            setattr(self, field.name, self.raw_data[field.name])
