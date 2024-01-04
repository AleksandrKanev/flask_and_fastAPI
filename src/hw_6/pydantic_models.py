from datetime import date
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str
    surname: str
    e_mail: str
    password: str


class UserOut(UserIn):
    id: int


class ProductIn(BaseModel):
    product_name: str
    description: str
    prise: float


class ProductOut(ProductIn):
    id: int


class OrderIn(BaseModel):
    id_user: int
    id_product: int
    order_date: date
    status_order: bool


class OrderOut(OrderIn):
    id: int
