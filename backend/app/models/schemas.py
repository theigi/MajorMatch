from pydantic import BaseModel, Field

class StudentData(BaseModel):
    math: float = Field(..., ge=0, le=100)
    physics: float = Field(..., ge=0, le=100)
    chemistry: float = Field(..., ge=0, le=100)
    english: float = Field(..., ge=0, le=100)
    interest: str

class PredictionResponse(BaseModel):
    major: str