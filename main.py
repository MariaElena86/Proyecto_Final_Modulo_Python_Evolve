from src.config import *
from src.io import *
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns
from src.viz import plot_graph
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys

root_path = Path("..").resolve() 
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

def main():
    print("paso 1 - Cargar dataset")
    df = load_csv()
    print("paso 2 - Limpiar datos")
    df = clean(df)
    print("paso 3 - Crear features")
    df = build_features(df)
    print("paso 4 - Mostrar gráficos")
    plot_graph(df)
    print("paso 5 - Exportar dataframe")
    export_to_csv(df)


if __name__ == "__main__":
    main()
