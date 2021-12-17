import pytest

from pydantic import ValidationError

from quadratic_equation import solve


@pytest.mark.parametrize(
    "args, result",
    [
        ((1, 0, 1), []),
        ((1, 0, -1), [1, -1]),
        ((1, 2, 1), [-1]),
    ]
)
def test_check_solvation(args, result):
    """
    1. для уравнения x^2+1 = 0 корней нет (возвращается пустой массив)
    2. для уравнения x^2-1 = 0 есть два корня кратности 1 (x1=1, x2=-1)
    3. для уравнения x^2+2x+1 = 0 есть один корень кратности 2 (x1= x2 = -1)
    """
    assert solve(*args) == result


def test_a_is_0_exceptions():
    with pytest.raises(ValidationError) as e:
        solve(0, 1, 1)
    assert e.value.errors()[0]['msg'] == 'argument "a" can not be a zero'


@pytest.mark.parametrize(
    'arg, error_msg',
    (
        (float('nan'), 'Argument "a" isnan'),
        (float('inf'), 'Argument "a" isinf'),
        (float('-inf'), 'Argument "a" isinf'),
    )
)
def test_invalid_args(arg, error_msg):
    with pytest.raises(ValidationError) as e:
        solve(arg, arg, arg)
    print(dir(e))
    assert e.value.errors()[0]['msg'] == error_msg
