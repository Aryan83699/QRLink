from pydantic import HttpUrl,BaseModel,Field
from typing import Annotated

class URL(BaseModel):
    url:Annotated[HttpUrl,Field(title="URL type checking",description="URL checking")]