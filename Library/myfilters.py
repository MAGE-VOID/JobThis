import pandas as pd
from typing import List, Dict, Any, Optional


def filter_by_date_posted(df: pd.DataFrame, days_back: Optional[int] = None) -> pd.DataFrame:
    if days_back is None or "date_posted" not in df.columns:
        return df

    df = df.copy()
    df["date_posted"] = pd.to_datetime(df["date_posted"], errors="coerce")
    cutoff = pd.Timestamp.now() - pd.Timedelta(days=days_back)
    return df[df["date_posted"] >= cutoff]


def filter_by_keywords(
    df: pd.DataFrame,
    column: str,
    keywords: Optional[List[str]] = None,
    case_insensitive: bool = True,
    all_must_match: bool = False
) -> pd.DataFrame:
    if not keywords or column not in df.columns:
        return df

    df = df.copy()
    col_series = df[column].astype(str)
    if case_insensitive:
        col_series = col_series.str.lower()
        keywords = [kw.lower() for kw in keywords]

    if all_must_match:
        mask = col_series.apply(lambda text: all(kw in text for kw in keywords))
    else:
        mask = col_series.apply(lambda text: any(kw in text for kw in keywords))

    return df[mask]


def filter_out_negative_phrases(
    df: pd.DataFrame,
    column: str,
    negatives: Optional[List[str]] = None,
    case_insensitive: bool = True,
) -> pd.DataFrame:
    if not negatives or column not in df.columns:
        return df

    df = df.copy()
    col_series = df[column].astype(str)
    if case_insensitive:
        col_series = col_series.str.lower()
        negatives = [neg.lower() for neg in negatives]

    mask_negative = col_series.apply(lambda text: any(neg in text for neg in negatives))
    return df[~mask_negative]


def filter_by_in_list(
    df: pd.DataFrame,
    column: str,
    values: Optional[List[str]] = None,
    partial_match: bool = False,
    case_insensitive: bool = True,
) -> pd.DataFrame:
    if not values or column not in df.columns:
        return df

    df = df.copy()
    col_series = df[column].astype(str)
    if case_insensitive:
        col_series = col_series.str.lower()
        values = [v.lower() for v in values]

    if partial_match:
        mask = col_series.apply(lambda text: any(v in text for v in values))
    else:
        mask = col_series.isin(values)

    return df[mask]


def truncate_column(df: pd.DataFrame, column: str, max_length: int = 77) -> pd.DataFrame:
    if column not in df.columns:
        return df.copy()

    df = df.copy()
    df[column] = df[column].astype(str).apply(
        lambda text: text if len(text) <= max_length else text[:max_length] + "..."
    )
    return df


def apply_filters(df: pd.DataFrame, filter_params: Dict[str, Any]) -> pd.DataFrame:
    """
    Aplica secuencialmente los filtros que se hayan definido en filter_params.
    """
    df_filtered = df.copy()

    # Ejemplo de cómo usar los parámetros (ajusta según tus necesidades):
    df_filtered = filter_by_date_posted(df_filtered, filter_params.get("days_back"))

    df_filtered = filter_by_keywords(
        df=df_filtered,
        column="description",
        keywords=filter_params.get("keywords_in_description"),
        case_insensitive=True,
        all_must_match=False,
    )

    df_filtered = filter_out_negative_phrases(
        df=df_filtered,
        column="description",
        negatives=filter_params.get("negatives_in_description"),
        case_insensitive=True,
    )

    df_filtered = filter_by_in_list(
        df=df_filtered,
        column="title",
        values=filter_params.get("title_keywords"),
        partial_match=True,
        case_insensitive=True,
    )

    df_filtered = filter_out_negative_phrases(
        df=df_filtered,
        column="title",
        negatives=filter_params.get("negatives_in_title"),
        case_insensitive=True,
    )

    df_filtered = filter_by_in_list(
        df=df_filtered,
        column="country",
        values=filter_params.get("country_list"),
        partial_match=False,
        case_insensitive=True,
    )

    return df_filtered

