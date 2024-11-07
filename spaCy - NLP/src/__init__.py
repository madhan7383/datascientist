# __init__.py

# This file marks the directory as a Python package.
# You can add package-level imports or initialization code here.

from .data_preprocessing import clean_text
from .entity_recognition import extract_entities
from .post_processing import filter_entities
from .model_trainer import train_model
from .extractor import extract_contact_info
from .utils import visualize_entities, evaluate_performance

# Optionally, you can define package-level variables or functions that will be accessible
# when importing the package as a whole. For example:
__all__ = [
    "clean_text",
    "extract_entities",
    "filter_entities",
    "train_model",
    "extract_contact_info",
    "visualize_entities",
    "evaluate_performance"
]
 
