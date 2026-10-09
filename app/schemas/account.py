from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class AccountCreate(BaseModel):
    customer_id: int
    account_number: str
    account_type: str


class AccountResponse(BaseModel):
    id: int
    customer_id: int
    account_number: str
    account_type: str
    balance: Decimal
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }