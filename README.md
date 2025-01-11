# JobThis

**JobThis** es un proyecto de **scraping** y **filtrado** de ofertas de trabajo, basado en la librería [JobSpy](https://github.com/Bunsly/JobSpy). Permite recopilar anuncios de sitios (Indeed, Glassdoor, ZipRecruiter) y luego aplicar filtros configurables para obtener solo los puestos que verdaderamente te interesan.

## Características

*   **Scraping multiplataforma**: Se apoya en [JobSpy](https://github.com/Bunsly/JobSpy) para extraer datos de diversas fuentes.
*   **Filtros flexibles**: Definidos en `filter_params.py` y aplicados en `myfilters.py`.
*   **Resultados paginados**: Muestra los trabajos en grupos de 10 filas, facilitando la revisión.
*   **Modularidad**: Código organizado en módulos (`Scrap.py`, `myfilters.py`, `filter_params.py`, etc.).

## Requisitos

Las dependencias necesarias están en `requirements.txt`: