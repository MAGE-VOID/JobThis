import warnings
import logging
from bs4 import MarkupResemblesLocatorWarning
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

from JobSpy import scrape_jobs
from JobSpy.jobs import Country


class JobScraper:
    """
    Clase que encapsula la lógica para:
      - Deshabilitar los loggers internos de JobSpy.
      - Definir sitios y países a consultar.
      - Realizar la consulta con tqdm y sumar resultados, usando multithreading.
      - Filtrar DataFrames para quedarse solo con las columnas relevantes.
    """

    DESIRED_COLS = [
        "title",
        "job_type",
        "interval",
        "min_amount",
        "max_amount",
        "job_url",
        "description",
        "date_posted",
        "country",
    ]

    def __init__(
        self,
        exclude_countries=None,
        sites_to_query=None,
        results_wanted=20,
        verbose=0,
        max_workers=5,
    ):
        """
        Inicializa el JobScraper.
          :param exclude_countries: Lista de países (en minúsculas) que NO deseas incluir.
          :param sites_to_query:    Lista de sitios a consultar.
          :param results_wanted:    Número de resultados deseados por país/sitio.
          :param verbose:           Nivel de verbosidad para JobSpy (0,1,2).
          :param max_workers:       Número de hilos para ejecutar peticiones en paralelo.
        """
        self.exclude_countries = exclude_countries or ["venezuela"]
        self.sites_to_query = sites_to_query or ["indeed", "glassdoor", "zip_recruiter"]
        self.results_wanted = results_wanted
        self.verbose = verbose
        self.max_workers = max_workers

        self.disable_jobspy_loggers()

        self.all_dfs = []

    def disable_jobspy_loggers(self):
        """
        Recorre todos los loggers y si comienzan con 'JobSpy', los deshabilita por completo.
        """
        for name in logging.root.manager.loggerDict:
            if name.startswith("JobSpy"):
                logger = logging.getLogger(name)
                logger.disabled = True
                logger.handlers.clear()
                logger.propagate = False

    def collect_countries(self):
        """
        Devuelve la lista de países (en minúsculas) excluyendo los definidos en self.exclude_countries.
        """
        valid_countries = []
        for country_enum in Country:
            name_in_lower = country_enum.value[0].split(",")[0].strip().lower()
            if name_in_lower not in self.exclude_countries:
                valid_countries.append(name_in_lower)
        return valid_countries

    def _scrape_single_df(self, country_str, site) -> pd.DataFrame:
        """
        Ejecuta scrape_jobs para un (país, sitio) y retorna un DataFrame filtrado con columnas deseadas.
        Además, asigna la columna 'country' con el país correspondiente.
        Si falla, retorna DataFrame vacío.
        """
        try:
            df_site = scrape_jobs(
                site_name=site,
                search_term=None,
                location=None,
                distance=50,
                is_remote=False,
                results_wanted=self.results_wanted,
                country_indeed=country_str,
                verbose=self.verbose,
            )
        except Exception:
            # Retorna DataFrame vacío si hay error
            return pd.DataFrame(columns=self.DESIRED_COLS)

        # Seleccionamos solo columnas deseadas que existan en df_site
        existing_cols = [c for c in self.DESIRED_COLS if c in df_site.columns]
        df_filtered = df_site[existing_cols].copy()

        # Agregamos/forzamos la columna 'country', para tenerla en el DF final
        df_filtered["country"] = country_str

        return df_filtered

    def run_scraping(self) -> pd.DataFrame:
        """
        Ejecuta el scraping país-por-país, sitio-por-sitio de forma *paralela*,
        mostrando el progreso con tqdm y actualizando el conteo global.
        Al final, concatena todo en un DataFrame con las columnas importantes.
        """
        countries_to_process = self.collect_countries()

        tasks = []
        for country_str in countries_to_process:
            for site in self.sites_to_query:
                tasks.append((country_str, site))

        total_iterations = len(tasks)
        total_jobs_global = 0

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor, tqdm(
            total=total_iterations, ncols=120, dynamic_ncols=False
        ) as pbar:

            future_to_task = {
                executor.submit(self._scrape_single_df, country, site): (country, site)
                for (country, site) in tasks
            }

            for future in as_completed(future_to_task):
                country, site = future_to_task[future]

                pbar.set_description_str(f"Analizando {site} - {country}")

                df_filtered = pd.DataFrame(columns=self.DESIRED_COLS)
                try:
                    df_filtered = future.result()
                except Exception:
                    pass  # Se queda df vacío

                # Acumulamos en self.all_dfs
                self.all_dfs.append(df_filtered)
                site_count = len(df_filtered)
                total_jobs_global += site_count

                pbar.set_postfix_str(f"jobs={total_jobs_global}")
                pbar.update(1)

        # Excluimos dataframes vacíos para evitar warnings de concat
        # 1) Excluimos DataFrames completamente vacíos
        valid_dfs = []
        for df in self.all_dfs:
            # si deseas eliminar columnas all-NA (opcional)
            df = df.dropna(axis=1, how="all")
            if not df.empty:
                valid_dfs.append(df)

        # 2) Concatenamos si hay al menos uno
        if valid_dfs:
            # sort=False evita reordenar las columnas
            final_df = pd.concat(valid_dfs, ignore_index=True, sort=False)
        else:
            final_df = pd.DataFrame(columns=self.DESIRED_COLS)

        print(
            f"\nTOTAL de trabajos (excluyendo {self.exclude_countries}): {total_jobs_global}"
        )
        print(f"Final DataFrame shape: {final_df.shape} (filas, columnas)\n")

        return final_df
