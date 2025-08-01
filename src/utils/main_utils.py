import sys
from typing import Dict, Tuple
import os
import pandas as pd
import pickle
import yaml
import boto3
from typing import Any

from src.constant import *
from src.exception import CustomException
from src.logger import logging

class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, filename: str) -> dict:
        try:
            with open(filename, "r") as yaml_file:  # Changed from "rb" to "r"
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise CustomException(e) from e  # Removed sys argument

    def read_schema_config_file(self) -> dict:
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))
            return schema_config

        except Exception as e:
            raise CustomException(e) from e  # Removed sys argument

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method of MainUtils class")

        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)

            logging.info("Exited the save_object method of MainUtils class")

        except Exception as e:
            
            raise CustomException(e) from e  # Removed sys argument

    @staticmethod
    def load_object(file_path: str) -> Any:
        logging.info("Entered the load_object method of MainUtils class")

        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)

            logging.info("Exited the load_object method of MainUtils class")
            return obj

        except Exception as e:
            raise CustomException(e) from e
