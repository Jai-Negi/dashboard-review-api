from fastapi import APIRouter, Form, File, UploadFile, HTTPException
from app.services.review_service import ReviewService
from app.services.s3_service import S3Service
from app.core.config import settings

router = APIRouter()

s3 = S3Service(
    aws_access_key = settings.AWS_ACCESS_KEY_ID,
    aws_secret_key = settings.AWS_SECRET_ACCESS_KEY,
    bucket_name = settings.S3_BUCKET_NAME
)

review_service = ReviewService(s3_service = s3)

@router.post("/submit-review")
async def submit_review(
    reviewer_name: str = Form(...),
    dashboard_link: str = Form(...),
    review_text: str = Form(""),
    file: UploadFile = File(None)
):
    """
    Accepts a review with optional text and/or uploaded file.
    Stores review in S3 and returns a review ID.
    """
    try:
        review_id = review_service.submit_review(
            reviewer_name=reviewer_name,
            dashboard_link=dashboard_link,
            review_text=review_text,
            file=file
        )
        return {"review_id": review_id, "status": "uploaded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))