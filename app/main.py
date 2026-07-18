from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="OpsPilot API",
    description="API for managing support incidents.",
    version="0.1.0",
)


class IncidentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=2000)
    requester: str = Field(min_length=2, max_length=100)


class IncidentResponse(IncidentCreate):
    id: int
    status: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/incidents",
    response_model=IncidentResponse,
    status_code=201,
)
def create_incident(incident: IncidentCreate) -> IncidentResponse:
    return IncidentResponse(
        id=1,
        status="open",
        **incident.model_dump(),
    )