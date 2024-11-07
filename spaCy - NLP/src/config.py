import os

# --- Directory Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for data, models, and other resources
DATA_DIR = os.path.join(BASE_DIR, 'data')
SAMPLE_DATA_DIR = os.path.join(DATA_DIR, 'sample_data')
ANNOTATIONS_DIR = os.path.join(DATA_DIR, 'annotations')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
SPACY_MODEL_DIR = os.path.join(MODELS_DIR, 'spacy_model')

# --- SpaCy Model Configuration ---
SPACY_MODEL_NAME = "en_core_web_trf"  # Pre-trained transformer-based model (you can use a different model if needed)
USE_GPU = True  # Set to False if you're not using a GPU

# --- Training Hyperparameters ---
TRAIN_BATCH_SIZE = 16  # The batch size used for training
TRAIN_EPOCHS = 10  # Number of training epochs
LEARNING_RATE = 0.001  # Learning rate for training the model

# --- Contact Extraction Configuration ---
EXTRACTION_CONFIG = {
    'extract_names': True,
    'extract_emails': True,
    'extract_phones': True,
    'extract_job_titles': True,
    'extract_companies': True,
    'regex_phone_pattern': r'\(?\+?\d{1,3}\)?[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{1,4}[\s\-]?\d{1,4}'
}

# --- Logging Configuration ---
LOGGING_LEVEL = 'INFO'  # Logging level can be DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'app.log')

# --- External API Keys / Configurations (if applicable) ---
# F
 
