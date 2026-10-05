from sqlalchemy.orm import Session

from app.models.customer import Customer


def create_customer(db: Session, customer: Customer) -> Customer:
    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer