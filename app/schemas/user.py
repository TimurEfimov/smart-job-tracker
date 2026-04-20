from pydantic import BaseModel, ConfigDict, Field


class UserCreateRequest(BaseModel):
    username: str = Field(..., max_length=127)
    password: str = Field(..., max_length=127)

    model_config = ConfigDict(from_attributes=True)