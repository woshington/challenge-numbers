from fastapi import FastAPI

from packages.domain.controllers.numbers_controller import NumberController
from packages.domain.services.numbers_service import NumbersService

app = FastAPI()
numbers_controller = NumberController(
    service=NumbersService()
)
app.include_router(
    numbers_controller.router,
    tags=["numbers"]
)