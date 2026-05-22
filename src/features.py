import pandas as pd
import numpy as np

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    #1. Nueva columna Year
    df_feature = add_year_feature(df)
   
    #2. Nueva columna ROI
    df_feature = add_roi_feature(df_feature)

    #3. Nueva columna categorica basada en el **ROI**
    df_feature = add_roi_category(df_feature)

    #4. Transforma la columna ``genres`` en formato lista.
    df_feature = transform_genres(df_feature)

    print("End Features:\n",df_feature.columns)
    return df_feature

def add_year_feature(df: pd.DataFrame) -> pd.DataFrame:
    # Crea una nueva columna 'year' a partir de 'release_date'.

    df = df.copy()
    # Convertir a datetime (errores → NaT)    
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    # Crear columna year
    df["year"] = df["release_date"].dt.year.astype("Int64")
    # Rellenar NaN con 0
    df["year"] = df["year"].fillna(0).astype("Int64")
    return df


def add_roi_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea una columna ROI basada en revenue y budget.
    ROI = (revenue - budget) / budget
    """

    df = df.copy()

    # Calcular usando .where(condición, valor_si_true, valor_si_false)
    df["roi"] = np.where(df["budget"] > 0,
                         (df["revenue"] - df["budget"]) / df["budget"],
                         0)

    return df

def add_roi_percentage(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea una columna basada en el ROI en %
    """
    df = df.copy()
    df['roi%'] = (df['roi'] * 100).round(2)
    return df

def add_roi_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea una columna categórica de ROI con 3 niveles:
    - Pedida (ROI < 0)
    - Media (0 ≤ ROI < 1)
    - Alta (ROI >= 1)
    """

    df = df.copy()

    df["roi_category"] = pd.cut(
        df["roi"],
        bins=[-float("inf"), 0, 1, float("inf")],
        labels=["Pedida", "Media", "Alta"],
        right=True,
        include_lowest=True
    )

    return df

def clean_genre_string(x):
    """
    Convierte un string de géneros en lista limpia usando lambda.
    """

    if not isinstance(x, str):
        return []

    genres = x.split(",")
    clean_genres = list(
        filter(
            lambda g: g.strip() != "",
            map(lambda g: g.strip(), genres)
        )
    )
    return clean_genres

def transform_genres(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma la columna 'genres' en una lista limpia de géneros.

    Ejemplo:
    "Action, Drama" → ["Action", "Drama"]

    Maneja valores nulos y limpia espacios.
    """
    df = df.copy()

    df["genres"] = df["genres"].fillna("").apply(clean_genre_string)

    return df