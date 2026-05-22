import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(df: pd.DataFrame) -> None:
    scatterplot_q1(df)
    barplot_q2(df)
    boxplot_q3(df)
    scatterplot_q4(df)
    scatterplot_q5(df)

#Q1. ¿Mayor inversión genera ROI positivo?
def scatterplot_q1(df: pd.DataFrame) -> None:
    df_q1 = df.dropna(subset=['budget', 'roi'])

    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df_q1, x='budget', y='roi', alpha=0.6)
    sns.regplot(data=df_q1, x='budget', y='roi', scatter=False, lowess=True, color='red', line_kws={'linewidth': 2})

    plt.xscale('log')
    plt.xlabel('Presupuesto (Budget)')
    plt.ylabel('Retorno de inversión (ROI)')
    plt.title('Relación entre Presupuesto y ROI')
    plt.tight_layout()

#Q2 ¿Qué género de películas tiene mayor presupuesto?
def barplot_q2(df: pd.DataFrame) -> None:
    genre_budget = (
    df.dropna(subset=['genres', 'budget'])
                .explode('genres')
                .groupby('genres')['budget']
                .mean()
                .sort_values(ascending=False)
    )

    plt.figure(figsize=(14, 6))
    sns.barplot(x=genre_budget.index[:20], y=genre_budget.values[:20], palette='viridis')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Género')
    plt.ylabel('Presupuesto (Budget)')
    plt.title('Top 20 géneros por presupuesto promedio')
    plt.tight_layout()

# Q3. ¿Qué género de películas tiene mayor ROI?
def boxplot_q3(df: pd.DataFrame) -> None:
    genre_roi = (
    df.dropna(subset=['genres', 'roi'])
            .explode('genres')
            .groupby('genres')['roi']
            .mean()
            .sort_values(ascending=False)
    )

    plt.figure(figsize=(14, 6))
    sns.barplot(x=genre_roi.index[:20], y=genre_roi.values[:20], palette='viridis')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Género')
    plt.ylabel('Rentabilidad (ROI) promedio')
    plt.title('Top 20 géneros por rentabilidad promedio')
    plt.tight_layout()

# Q4. ¿La película más popular es la que más ROI tiene?
def scatterplot_q4(df: pd.DataFrame) -> None:
    df_q4 = df.dropna(subset=['popularity', 'vote_average', 'roi'])

    plt.figure(figsize=(14, 6))
    scatter = plt.scatter(data=df_q4, x='popularity', y='vote_average', 
                        c='roi', s=100, alpha=0.6, cmap='RdYlGn', edgecolors='black', linewidth=0.5)
    plt.colorbar(scatter, label='ROI')
    plt.xlabel('Popularidad')
    plt.ylabel('Calificación de la crítica (vote_average)')
    plt.title('Relación entre Popularidad, Calificación y ROI')
    plt.xscale('log')
    plt.tight_layout()
    plt.show()

# Q5. ¿Cuáles son las "joyas escondidas" (alta valoración, alto ROI y baja popularidad)?
def scatterplot_q5(df: pd.DataFrame) -> None:
    df_hidden = df[(df['roi'] > 2) & (df['vote_average'] > 7)]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df_hidden,
        x='vote_average',
        y='roi',
        hue='roi',
        palette='coolwarm',
        alpha=0.7,
        edgecolor='w',
        linewidth=0.5
    )
    sns.regplot(
        data=df_hidden,
        x='vote_average',
        y='roi',
        scatter=False,
        color='black',
        line_kws={'linewidth': 1.5},
        lowess=True
    )
    plt.yscale('symlog')
    plt.xlabel('Valoración Crítica (vote_average)')
    plt.ylabel('Retorno de Inversión (ROI)')
    plt.title('Relación entre valoración y ROI')
    plt.legend([], [], frameon=False)
    plt.tight_layout()
    plt.show()