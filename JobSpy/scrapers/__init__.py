from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, List, Union

from ..jobs import (
    Enum,
    BaseModel,
    JobType,
    JobResponse,
    Country,
    DescriptionFormat,
)


class Site(Enum):
    LINKEDIN = "linkedin"
    INDEED = "indeed"
    ZIP_RECRUITER = "zip_recruiter"
    GLASSDOOR = "glassdoor"
    GOOGLE = "google"


class SalarySource(Enum):
    DIRECT_DATA = "direct_data"
    DESCRIPTION = "description"


class ScraperInput(BaseModel):
    site_type: List[Site]
    search_term: Optional[str] = None
    google_search_term: Optional[str] = None

    location: Optional[str] = None
    country: Optional[Country] = Country.USA
    distance: Optional[int] = None
    is_remote: bool = False
    job_type: Optional[JobType] = None
    easy_apply: Optional[bool] = None
    offset: int = 0
    linkedin_fetch_description: bool = False
    linkedin_company_ids: Optional[List[int]] = None
    description_format: Optional[DescriptionFormat] = DescriptionFormat.MARKDOWN

    results_wanted: int = 15
    hours_old: Optional[int] = None


class Scraper(ABC):
    def __init__(
        self,
        site: Site,
        proxies: Optional[List[str]] = None,
        ca_cert: Optional[str] = None,
    ):
        self.site = site
        self.proxies = proxies
        self.ca_cert = ca_cert

    @abstractmethod
    def scrape(self, scraper_input: ScraperInput) -> JobResponse:
        ...
