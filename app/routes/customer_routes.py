from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.services.customer_service import create_customer_service


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