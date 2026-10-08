from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.account import AccountCreate, AccountResponse
from app.services.account_service import create_account_service


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post(
    "/",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED
)
def create_account(
    account_data: AccountCreate,
    db: Session = Depends(get_db)
):
    return create_account_service(db, account_data)