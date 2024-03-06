from pydantic import BaseModel


class CreateToDoRequest(BaseModel):
    content : str
    is_done : bool