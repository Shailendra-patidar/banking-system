from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.repositories.customer_repository import create_customer, delete_customer, get_customer
from app.schemas.customer import CustomerCreate


def create_customer_service(
    db: Session,
    customer_data: CustomerCreate
) -> Customer:
    customer = Customer(
        full_name=customer_data.full_name,
        email=customer_data.email,
        phone=customer_data.phone,
        address=customer_data.address,
    )

    return create_customer(db, customer)


def get_customer_service(
    db: Session,
    customer_id: int
) -> Customer | None:
    return get_customer(db, customer_id)

def delete_customer_service(
    db: Session,
    customer_id: int
) -> Customer | None:
    return delete_customer(db, customer_id)