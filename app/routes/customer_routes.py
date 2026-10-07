from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.services.customer_service import create_customer_service, delete_customer_service, get_customer_service, update_customer_service


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post(
    "/",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_customer(
    customer_data: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer_service(db, customer_data)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return get_customer_service(db, customer_id)


@router.delete(
    "/{customer_id}",
    response_model=CustomerResponse
)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return delete_customer_service(db, customer_id)


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
    status_code=status.HTTP_200_OK
)
def update_customer(
    customer_id: int,
    customer_data: CustomerCreate,
    db: Session = Depends(get_db)
):
    customer = update_customer_service(
        db,
        customer_id,
        customer_data
    )

    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return customer