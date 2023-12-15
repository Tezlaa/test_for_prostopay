from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserType(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    username: str
    
    
class UserDTO(UserType):
    id: Optional[int]