import yaml
import random
import numpy as np
from pathlib import Path
from typing import Dict, Any


def load_config(path: str) -> Dict[str, Any]:
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
