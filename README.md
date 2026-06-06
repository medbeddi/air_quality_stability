# Air Quality Stability

Projet scientifique reproductible — Module Science des Données et Calcul Scientifique Avancé.

## Installation de l'environnement

```bash
mamba env create -f environment.yml
mamba activate air_quality_stability
```

## Lancer le pipeline complet

```bash
python -m src.main
```

## Lancer les tests

```bash
pytest tests/
```

## Structure du projet

```
air_quality_stability/
├── configs/config.yaml       # Hyperparamètres externalisés
├── data/raw/                 # Données brutes (non versionnées)
├── outputs/figures/          # Graphiques générés
├── scripts/                  # Exercices stabilité numérique
├── src/
│   ├── main.py               # Orchestrateur principal
│   ├── preprocessing.py      # Nettoyage + split + scaling
│   └── utils.py              # Chargement config, seed
├── tests/
│   └── test_preprocessing.py # Tests unitaires pytest
├── environment.yml
└── .gitignore
```
