from pydantic import BaseModel

class Forms(BaseModel):
    title: str
    category: str
    url: str
    attention: str