## Análisis de Producciones Cinematográfica
### Origen de los datos:
Para este estudio, se ha seleccionado un dataset masivo que recopila la información de producciones cinematográficas globales.

Dataset `The Ultimate 1Million Movies Dataset (TMDB + IMDb)`  [Kaggle](https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates?select=TMDB_all_movies.csv), utilizando el fichero unificado TMDB_all_movies.csv

Dataset con un total de filas y columnas inicial: (filas=1196662, columnas=28)

### Objetivo
El objetivo de este proyecto es realizar un análisis exploratorio de los datos sobre un dataset de películas de TMDB (The Ultimate 1 Million Movies Dataset). 

Se aplicará un proceso de análisis de datos que incluye limpieza, transformación y generación de nuevas características, con el objetivo de enriquecer la información disponible y facilitar la extracción de insights.

Finalmente, se utilizarán visualizaciones para explorar relaciones entre variables y responder preguntas relacionadas con el éxito económico, la recepción del público y las tendencias dentro de la industria.

### Pipeline a seguir: 
***load → clean → features → viz → export***


### Variables a analizar:

| Variables      | Descripción |
| -----------------------------| ------------|
| `budget`       | Presupuesto de producción de la película |
| `revenue`      | Ingresos totales generados por la película |
| `popularity`   | Índice de popularidad calculado por TMDB que mide el interés generado en la plataforma (visualizaciones, votos, favoritos, watchlist e interacción) |
| `vote_average` | Valoración media de los usuarios en TMDB (escala de 0 a 10), representa la calidad percibida  |
| `vote_count`   | Número total de votos recibidos en TMDB |
| `title`     | Título de la película  |
| `genres`    | Géneros a los que pertenece la película (puede contener múltiples valores) |
| `original_language` | Idioma original de la película   |
|`production_companies`| Compañías productoras involucradas en la película.|
| `release_date` | Fecha de estreno de la película |


### Preguntas para realizar el análisis
- Q1. ¿Mayor inversión genera ROI positivo?
- Q2. ¿Qué género de películas tiene mayor presupuesto?
- Q3. ¿Qué género de películas tiene mayor ROI?
- Q4. ¿La película más popular es la que más ROI tiene?
- Q5. ¿Cuáles son las "joyas escondidas" (alta valoración, alto ROI)?
  

### Limpieza de los datos
Eliminación de columnas que no son necesarias para el análisis.

[``imdb_id``, ``overview``, ``tagline``, ``poster_path``,  ``cast``,
    ``director_of_photography``, ``writers``, ``producers``, ``music_composer``,
    ``spoken_languages``, ``production_countries``, ``original_language``,
    ``imdb_rating``, ``imdb_votes``]

Transformar variables  numéricas a formato int 

[``budget``, ``revenue``, ``vote_count``, ``runtime``, ``popularity``, ``vote_average``]

Filtrar la columna (``runtime``)  > 60 para obtener solo las peliculas.

Filtrar las columnas (``budget, revenue``) con valor > 0 para calcular metricas.

### Crear Features
Adicionar nueva columna con el año de la publicacion.

Adicionar nueva columna con el calculo del ROI(Retorno de Inversión)

   formula = $$ROI = \frac{Revenue - Budget}{Budget}$$

| ROI       | Tipo             | Interpretación                                                      |
| --------- | ---------------- | ------------------------------------------------------------------- |
| 0.064339  | Positivo pequeño | La película ganó un 6.4% más de lo invertido                        |
| -0.422051 | Negativo         | La película perdió aproximadamente un 42.2% del presupuesto         |
| 11.316140 | Muy alto         | La película ganó un 1131% del presupuesto (≈ 11 veces lo invertido) |

Adicionar nueva columna categorica basada en el ROI
   
| Categoría          | Rango de ROI | Interpretación                     |
| ------------------ | ------------ | ---------------------------------- |
| ***loss***         | ROI < 0      | La película pierde dinero          |
| ***low_revenue***  | 0 ≤ ROI < 1  | Recaudación baja o moderada        |
| ***high_revenue*** | ROI ≥ 1      | Recaudación alta / éxito comercial |

Transforma la columna ``genres`` en formato lista.


### Cómo ejecutar
- `pip install -r requirements.txt`
- Ejecutar pipeline: `python main.py`
- (Opcional) Abrir y ejecutar: `notebooks/eda.ipynb`
