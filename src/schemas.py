from pydantic import BaseModel

class DataCreate(BaseModel):
    data: str
