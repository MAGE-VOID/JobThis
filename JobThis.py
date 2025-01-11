import logging
import warnings
import pandas as pd
from bs4 import MarkupResemblesLocatorWarning

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)
logging.getLogger("JobSpy:Google").setLevel(logging.ERROR)
logging.getLogger("JobSpy:Glassdoor").setLevel(logging.ERROR)

# Importa la clase JobScraper
from Library.JobScraperModule import JobScraper

# Importa los filtros y la función apply_filters
from Library.myfilters import (
    apply_filters,
    truncate_column,
)

# Importa el diccionario de parámetros de filtrado
from filter_params import filter_parameters


def paginate_and_display(df: pd.DataFrame, page_size: int = 10):
    """
    Muestra un DataFrame de 10 en 10 filas (por defecto),
    preguntando si deseas continuar con la siguiente página.
    """
    start_index = 0
    total_rows = len(df)

    while True:
        end_index = start_index + page_size
        # Extraemos la "página" actual
        subset = df.iloc[start_index:end_index]

        if subset.empty:
            print("No hay más filas por mostrar.")
            break

        print(subset)  # Muestra la página actual
        start_index = end_index

        if start_index >= total_rows:
            print("Has llegado al final de los resultados.")
            break

        user_input = input("\nPresiona [Enter] para ver la siguiente página o 'q' para salir: ")
        if user_input.lower() == 'q':
            print("Saliendo de la paginación.")
            break

def main():
    # 1) Configura el scraper
    scraper = JobScraper(
        exclude_countries=["venezuela"],  
        sites_to_query=["indeed", "glassdoor", "zip_recruiter"],
        results_wanted=100,
        verbose=0,
        max_workers=5,
    )
    raw_df = scraper.run_scraping()

    # 2) Aplica los filtros desde filter_params
    final_df = apply_filters(raw_df, filter_parameters)

    # 3) Truncar la columna de descripción
    final_df = truncate_column(final_df, "description", 77)

    # 4) Mostrar resultados con paginación
    pd.set_option("display.max_colwidth", None)
    print("Resultados filtrados:")
    print(f"Cantidad de trabajos finales: {len(final_df)}\n")

    # Llamamos a la función de paginación
    paginate_and_display(final_df, page_size=10)


if __name__ == "__main__":
    main()
