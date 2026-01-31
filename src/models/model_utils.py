import os

def model_exists(model_path):
    """
    Check if trained model exists
    """
    return os.path.exists(model_path)
