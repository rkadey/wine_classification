from wine_project.entity.config_entity import ModelEvaluationConfig
from wine_project.entity.artifact_entity import ModelTrainerArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from sklearn.metrics import f1_score
from wine_project.exception import USvisaException
from wine_project.constants import TARGET_COLUMN, CURRENT_YEAR
from wine_project.logger import logging
import sys
import pandas as pd
from typing import Optional
from dataclasses import dataclass
from wine_project.entity.estimator import WineModel
from wine_project.entity.estimator import TargetValueMapping

@dataclass
class EvaluateModelResponse:
    trained_model_f1_score: float
    best_model_f1_score: float
    is_model_accepted: bool
    difference: float