from math import isnan, isinf, sqrt
from decimal import Decimal, getcontext

from pydantic import BaseModel, validator


class ArgsValidationSchema(BaseModel):
    a: float
    b: float
    c: float

    @validator('a')
    def a_is_not_zero(cls, v):
        if v == 0:
            raise ValueError('argument "a" can not be a zero')
        return v

    @validator('a', 'b', 'c')
    def validate_float(cls, v):
        for check in (isinf, isnan):
            if check(v):
                raise ValueError(f'Argument "a" {check.__name__}')
        return v


def solve(a: float, b: float, c: float, precision: int = 9) -> list:
    getcontext().prec = precision
    args = ArgsValidationSchema(**{'a': a, 'b': b, 'c': c})
    a, b, c = Decimal(args.a), Decimal(args.b), Decimal(args.c)
    discr: Decimal = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + Decimal(sqrt(discr))) / (2 * a)
        x2 = (-b - Decimal(sqrt(discr))) / (2 * a)
        return [x1, x2]
    elif discr == 0:
        x = -b / (2 * a)
        return [x]
    return []
