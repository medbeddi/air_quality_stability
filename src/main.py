import sys
import os
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from src.utils import load_config, set_seed


def main():
    config = load_config('configs/config.yaml')

    set_seed(config['project']['random_seed'])

    print("[RUN] Execution du pipeline scientifique...")
    print(f"[RUN] Projet : {config['project']['name']}")
    print(f"[RUN] Seed   : {config['project']['random_seed']}")


if __name__ == "__main__":
    main()
