# Необходимо создать базу данных для интернет-магазина. База данных должна
# состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
# содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных
# пользователях магазина. Таблица заказы должна содержать информацию о
# заказах, сделанных пользователями.

from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import create_engine, select, insert, update, delete
import databases

from .pydantic_models import UserIn, UserOut, ProductIn, ProductOut, OrderIn, OrderOut
from .sql_models import Base, User, Product, Order

DATABASE_URL = 'sqlite:///src/hw_6/task_6.sqlite'

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()

    yield

    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get('/')
async def index():
    users = await database.fetch_all(select(User))
    order = await database.fetch_all(select(Order))
    product = await database.fetch_all(select(Product))

    return {'user': users, 'order': order, 'product': product}


@app.post('/users/', response_model=UserIn)
async def create_user(user: UserIn):
    new_user = insert(User).values(**user.model_dump())
    await database.execute(new_user)

    return user


@app.get('/users/{user_id}', response_model=UserOut)
async def get_user(user_id: int):
    user = await database.fetch_one(select(User).where(User.id == user_id))
    return user


@app.put('/users/{user_id}', response_model=UserOut)
async def update_user(user_id: int, new_user: UserIn):
    user_update = (
        update(User)
        .where(User.id == user_id)
        .values(**new_user.model_dump())
    )
    await database.execute(user_update)

    return await database.fetch_one(select(User).where(User.id == user_id))


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    delete_user = delete(User).where(User.id == user_id)

    await database.execute(delete_user)

    return {'result': 'success', 'deleted_user_id': user_id}


@app.post('/product/', response_model=ProductIn)
async def create_product(product: ProductIn):
    new_product = insert(Product).values(**product.model_dump())
    await database.execute(new_product)

    return product


@app.get('/product/{product_id}', response_model=ProductOut)
async def get_product(product_id: int):
    product = await database.fetch_one(select(Product).where(Product.id == product_id))
    return product


@app.put('/product/{product_id}', response_model=ProductOut)
async def update_product(product_id: int, new_product: ProductIn):
    product_update = (
        update(Product)
        .where(Product.id == product_id)
        .values(**new_product.model_dump())
    )
    await database.execute(product_update)

    return await database.fetch_one(select(Product).where(Product.id == product_id))


@app.delete('/product/{product_id}')
async def delete_prod(product_id: int):
    delete_product = delete(Product).where(Product.id == product_id)

    await database.execute(delete_product)

    return {'result': 'success', 'deleted_product_id': product_id}


@app.post('/order/', response_model=OrderIn)
async def create_order(order: OrderIn):
    new_order = insert(Order).values(**order.model_dump())
    await database.execute(new_order)

    return order


@app.get('/order/{order_id}', response_model=OrderOut)
async def get_order(order_id: int):
    order = await database.fetch_one(select(Order).where(Order.id == order_id))
    return order


@app.put('/order/{order_id}', response_model=OrderOut)
async def update_order(order_id: int, new_order: OrderIn):
    order_update = (
        update(Order)
        .where(Order.id == order_id)
        .values(**new_order.model_dump())
    )
    await database.execute(order_update)

    return await database.fetch_one(select(Order).where(Order.id == order_id))


@app.delete('/order/{order_id}')
async def delete_order(order_id: int):
    delete_order = delete(Order).where(Order.id == order_id)

    await database.execute(delete_order)

    return {'result': 'success', 'deleted_product_id': order_id}
