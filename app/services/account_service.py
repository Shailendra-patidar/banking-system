from sqlalchemy.orm import Session

from app.models.account import Account
from app.repositories.account_repository import create_account
from app.schemas.account import AccountCreate


def create_account_service(
    db: Session,
    account_data: AccountCreate
) -> Account:

    account = Account(
        customer_id=account_data.customer_id,
        account_number=account_data.account_number,
        account_type=account_data.account_type,
    )

    return create_account(db, account)