# app/services/review_service.py

import uuid
from app.models.review import Review
from fastapi import UploadFile

class ReviewService:
    def __init__(self, s3_service):
        self.s3 = s3_service

    def submit_review(self, reviewer_name: str, dashboard_link: str, review_text: str, file: UploadFile = None):
        # Create a unique review ID
        review_id = str(uuid.uuid4())

        # Create the review data dictionary
        review_data = {
            "review_id": review_id,
            "reviewer_name": reviewer_name,
            "dashboard_link": dashboard_link,
            "review_text": review_text
        }

        # Upload review JSON metadata to S3
        json_key = f"reviews/{review_id}.json"
        self.s3.upload_json(key=json_key, data=review_data)

        # Upload file if provided
        if file:
            file_key = f"reviews/{review_id}_{file.filename}"
            # file.file is a SpooledTemporaryFile, upload_fileobj expects a file-like object
            self.s3.upload_file(key=file_key, file_obj=file.file)

        return review_id
