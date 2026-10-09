from fastapi import APIRouter, Depends, HTTPException, status
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
    account = create_account_service(db, account_data)

    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return account

