from packages.domain.models.numbers import Numbers
from pytest import mark, raises


class TestNumbers:
    @mark.asyncio
    async def test_sum(self):
        assert Numbers().sum([1, 2]) == 3

    @mark.asyncio
    async def test_average_without_exception(self):
        assert Numbers().average([7, 8, 9]) == 8