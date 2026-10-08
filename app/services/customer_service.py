from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.customer import Customer
from app.repositories.customer_repository import create_customer, delete_customer, get_customer, update_customer
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
) -> Customer:
    customer = delete_customer(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return customer


def update_customer_service(
    db: Session,
    customer_id: int,
    customer_data: CustomerCreate
) -> Customer | None:

    customer = get_customer(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
             detail="Customer not found"
        )

    customer.full_name = customer_data.full_name
    customer.email = customer_data.email
    customer.phone = customer_data.phone
    customer.address = customer_data.address

    return update_customer(db, customer)