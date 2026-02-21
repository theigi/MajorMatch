from fastapi import APIRouter, HTTPException, Response
from app.models.schemas import StudentData, PredictionResponse
from app.services.predictor import get_predictor
from app.services.pdf_generator import generate_report_pdf

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(data: StudentData):
    predictor = get_predictor()
    prediction = predictor.predict(
        data.math, data.physics, data.chemistry, data.english, data.interest
    )
    return {"major": prediction}

@router.post("/download-report")
async def download(data: StudentData):
    predictor = get_predictor()
    prediction = predictor.predict(
        data.math, data.physics, data.chemistry, data.english, data.interest
    )
    pdf_buffer = generate_report_pdf(data, prediction)
    return Response(
        content=pdf_buffer.getvalue(),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=MajorMatch_Report.pdf"}
    )