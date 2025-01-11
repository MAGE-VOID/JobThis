# JobThis

**JobThis** es una solución automatizada para **scraping** y **filtrado** de ofertas de trabajo, basada en la librería [JobSpy](https://github.com/Bunsly/JobSpy). Permite extraer ofertas de empleo de diversos portales (Indeed, Glassdoor, ZipRecruiter) y aplicar filtros ajustables para aislar únicamente aquellos puestos que se alineen con tus intereses.

---

## Tabla de Contenidos

1. [Características](#características)  
2. [Requisitos](#requisitos)  
3. [Instalación](#instalación)  
4. [Uso](#uso)  
5. [Configuración de Filtros](#configuración-de-filtros)  
6. [Estructura de Carpetas](#estructura-de-carpetas) *(opcional)*  
7. [Créditos](#créditos) *(opcional)*  

---

## Características

- **Scraping multiplataforma**: Emplea [JobSpy](https://github.com/Bunsly/JobSpy) para recopilar datos de varios sitios de empleo.  
- **Filtros flexibles**: Permite configurar criterios de búsqueda y exclusión en `filter_params.py`, aplicados a través de `myfilters.py`.  
- **Resultados paginados**: Muestra los resultados en grupos (por defecto, 10 filas), facilitando el desplazamiento entre muchas ofertas.  
- **Código modular**: Organizado en módulos (`Scrap.py`, `myfilters.py`, `filter_params.py`, etc.) para facilitar la mantenibilidad y escalabilidad.

---