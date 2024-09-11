from fastapi import APIRouter

from packages.domain.ports.numbers_service_interface import NumbersServiceInterface
from packages.domain.schemas.common import InputSchema, SumOutputSchema, AverageOutputSchema


class NumberController:
    def __init__(self, service: NumbersServiceInterface):
        self.service = service
        self.router = APIRouter()
        self.router.add_api_route(
            "/sum",
            self.__sum,
            methods=["POST"],
            response_model=SumOutputSchema,
            description="Sum numbers a list of integers and return the total"
        )
        self.router.add_api_route(
            "/average",
            self.__average,
            methods=["POST"],
            response_model=AverageOutputSchema,
            description="Average numbers a list of integers and return the average"
        )

    async def __sum(self, params: InputSchema):
        return await self.service.sum(params)

    async def __average(self, params: InputSchema):
        return await self.service.average(params)
