from sqlalchemy.orm import Session

from app.models.account import Account


def create_account(
    db: Session,
    account: Account
) -> Account:
    db.add(account)
    db.commit()
    db.refresh(account)

    return account