from datetime import datetime

from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    address: str | None = None


class CustomerResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    address: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }