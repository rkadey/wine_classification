import sys

from pandas import DataFrame
from sklearn.pipeline import Pipeline

from wine_project.exception import WineException
from wine_project.logger import logging

class TargetValueMapping:
    def __init__(self):
        self.low: int = 0
        self.medium:int = 1
        self.high:int = 2

    def _asdict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))