from pydantic import BaseModel, ConfigDict, Field, field_validator

class UserCreateRequest(BaseModel):
    username: str = Field(..., max_length=127)
    password: str = Field(..., max_length=127)

    @field_validator("username")
    def validate_username(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        return value
    
    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class UserResponse(UserCreateRequest):
    id: int
    model_config = ConfigDict(from_attributes=True)