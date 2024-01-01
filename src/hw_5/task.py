from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from models import Cars

app = FastAPI()
templates = Jinja2Templates("templates")
car_list: list[Cars] = []


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'car_list': car_list})


@app.post('/car/')
async def add_car(car: Cars):
    car_list.append(car)
    return car


@app.get('/car/{car_id}', response_class=HTMLResponse)
async def get_car(request: Request, car_id: int):
    filter_cars = [car for car in car_list if car_id == car.id]
    if not filter_cars:
        car = None
    else:
        car = filter_cars[0]

    return templates.TemplateResponse("car.html", {'request': request, 'car': car})


@app.put('/car/{car_id}')
async def update_car(car_id: int, new_car: Cars):
    for car in car_list:
        if car.id == car_id:
            car_list.remove(car)
            car_list.append(new_car)
            return {'updated': True}

    return {'updated': False}


@app.delete('/car/{car_id}')
async def delete_car(car_id: int):
    for car in car_list:
        if car.id == car_id:
            car_list.remove(car)
            return {'delete': True}

    return {'delete': False}
