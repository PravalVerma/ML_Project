import os
import sys
import pickle

import numpy as np
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from exception import CustomException

def save_object(file_path,obj):
    """
    This function is responsible for saving the objects
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
