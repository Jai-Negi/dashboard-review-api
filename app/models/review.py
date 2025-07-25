# app/models/review.py

from pydantic import BaseModel, HttpUrl
from typing import Optional

class Review(BaseModel):
    reviewer_name: str
    dashboard_link: HttpUrl
    review_text: Optional[str] = None
