## Banking
from calendar import month


def loan_cost_and_payment(amount: int, month_duration: int, yearly_rate: float) -> tuple[float, float]:
    """
    :param amount: total amount of the load
    :param month_duration: duration in month of the credit
    :param yearly_rate: yearly interest rate betweeon 0 and 1 (not percent)
    """
    assert type(amount) == int
    assert type(month_duration) == int
    assert type(yearly_rate) == float
    assert yearly_rate < 1
    assert yearly_rate >= 0

    monthly_rate = yearly_rate / 12

    denominator = (1 - (1 + monthly_rate) ** - month_duration)

    payment = amount*(monthly_rate/denominator)

    return payment, payment * month_duration - amount

def _loan_one_month(amount: int, monthly_payment, yearly_rate) -> tuple[float, float, float]:


    return 1, 1, 1

def loan_monthly_table(amount: int, month_duration: int, yearly_rate: float) -> list[list]:
    """
    :param amount: total amount of the load
    :param month_duration: duration in month of the credit
    :param yearly_rate: yearly interest rate betweeon 0 and 1 (not percent)
    """

    if month_duration == 0:
        return []
    else:
        balance, interest, principal = _loan_one_month(amount, month_duration, yearly_rate)
        return loan_monthly_table(amount, month_duration, yearly_rate)