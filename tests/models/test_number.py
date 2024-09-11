from packages.domain.models.numbers import Number
from pytest import mark, raises


class TestNumber:
    @mark.asyncio
    async def test_sum(self):
        assert Number().sum(1, 2) == 3

    @mark.asyncio
    async def test_divide_without_exception(self):
        from packages.domain.models.numbers import Number
        assert Number().divide(2, 2) == 1

    @mark.asyncio
    async def test_divide_with_division_by_zero(self):
        with raises(ZeroDivisionError):
            Number().divide(2, 0)