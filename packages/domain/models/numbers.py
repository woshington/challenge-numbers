import logging

logger = logging.getLogger(__name__)


class Number:
    @staticmethod
    def sum(a: int, b: int) -> int:
        logger.info(f"Summing {a} and {b}")
        return a + b

    @staticmethod
    def divide(a: int, b: int) -> float:
        logger.info(f"Dividing {a} by {b}")
        try:
            return a / b
        except ZeroDivisionError as exc:
            logger.info(f"Cannot divide {a} by {b}")
            raise exc


class Numbers:
    def __init__(self):
        self.number = Number()

    def sum(self, numbers: list[int]) -> int:
        total = 0
        for number in numbers:
            total = self.number.sum(total, number)
        return total

    def average(self, numbers: list[int]) -> float:
        return self.number.divide(sum(numbers), len(numbers))
