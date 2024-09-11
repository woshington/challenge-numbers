from pydantic import BaseModel, Field, field_validator


class InputSchema(BaseModel):
    numbers: list[int] = Field(min_items=2)


class SumOutputSchema(BaseModel):
    total: int = Field()


class AverageOutputSchema(BaseModel):
    average: float = Field()

    @field_validator('average')
    @classmethod
    def round(cls, v: float) -> float:
        return round(v, 3)