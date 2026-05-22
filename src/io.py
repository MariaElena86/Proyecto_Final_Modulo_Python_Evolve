from pathlib import Path
import pandas as pd
import sys

root_path = Path("..").resolve() 
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from src.io import *
from src.config import *


def load_csv():
    """Load a CSV file into a DataFrame."""
    df = pd.read_csv(RAW_PATH)
    return df


def export_to_csv(df: pd.DataFrame)  -> None:
    """Export DataFrame to CSV file into data/processed"""
    df.to_csv(OUT_PATH, index=False)