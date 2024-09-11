from abc import ABC, abstractmethod

from packages.domain.models.numbers import Numbers
from packages.domain.schemas.common import InputSchema, SumOutputSchema, AverageOutputSchema


class NumbersServiceInterface(ABC):
    def __init__(self):
        self.numbers_model = Numbers()

    @abstractmethod
    async def sum(self, params: InputSchema) -> SumOutputSchema:
        raise NotImplementedError

    @abstractmethod
    async def average(self, params: InputSchema) -> AverageOutputSchema:
        raise NotImplementedError
