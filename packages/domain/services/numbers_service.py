from packages.domain.ports.numbers_service_interface import NumbersServiceInterface
from packages.domain.schemas.common import InputSchema, AverageOutputSchema, SumOutputSchema


class NumbersService(NumbersServiceInterface):
    async def sum(self, params: InputSchema) -> SumOutputSchema:
        return SumOutputSchema(
            total=self.numbers_model.sum(params.numbers)
        )

    async def average(self, params: InputSchema) -> AverageOutputSchema:
        return AverageOutputSchema(
            average=self.numbers_model.average(params.numbers)
        )
