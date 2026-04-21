from pydantic import BaseModel, ConfigDict, Field

class UserCreateRequest(BaseModel):
    username: str = Field(..., max_length=127)
    password: str = Field(..., max_length=127)


class UserResponse(UserCreateRequest):
    id: int
    model_config = ConfigDict(from_attributes=True)