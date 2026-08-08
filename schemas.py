from pydantic import BaseModel
from typing import Optional

class AppealCreate(BaseModel):
    device_id: str
    yo_nalish: str
    matn: str

class AppealResponse(BaseModel):
    id: int
    AI_javobi: Optional[str] = None