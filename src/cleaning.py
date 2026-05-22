import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:    
    # 1- Eliminar columnas irrelevantes
    df = drop_columns(df)

    # 2- Convertir variables numéricas a tipos int
    df = convertir_a_enteros(df)

    # 3- Filtrar solo las peliculas con runtime > 60 
    df = filter_only_movies(df)

    # 4- Filtrar las columnas (``budget, revenue``) con valor > 0 para calcular el ROI.
    df = filter_numeric_columns(df)

    print("End Clean Data:\n",df.columns)
    return df


def drop_columns(df):
    drop_columns = [
        "imdb_id", "status", "original_title", "overview", "tagline", "poster_path",
        "cast", "director_of_photography","writers", "producers", "music_composer",
        "spoken_languages", "production_countries", "original_language","imdb_rating", "imdb_votes"
    ]
    df_clean = df.drop(columns=drop_columns, errors="ignore")
    return df_clean


def convertir_a_enteros(df):
    columns = ['budget', 'revenue', 'vote_count', 'runtime', 'popularity', 'vote_average']
    # Validar que las columnas existan en el DataFrame
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Columnas no encontradas en el DataFrame: {missing}")

    # Convertir a numérico y forzar errores a NaN
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')

    # Reemplazar NaN por 0 y convertir a int
    df[columns] = df[columns].fillna(0).astype(int)
    return df   

     
def filter_only_movies(df):
    # Filtrar solo las filas donde la columna runtime > 60, que son las peliculas
    df_movies = df[df['runtime'] > 70]
    return df_movies


def filter_numeric_columns(df):
    columns = ['budget','revenue']
    # Validar que las columnas existan en el DataFrame
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Columnas no encontradas en el DataFrame: {missing}")
    
    df_filter = df[(df[columns] > 0).all(axis=1)]
    return df_filter
