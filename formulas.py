## Banking
from calendar import month

def loan_total_cost_and_monthly_payment(amount: int, month_duration: int, yearly_rate: float) -> tuple[float, float]:
    """
    :param amount: total amount of the load
    :param month_duration: duration in month of the credit
    :param yearly_rate: yearly interest rate betweeon 0 and 1 (not percent)
    """
    monthly_rate = yearly_rate / 12

    denominator = (1 - (1 + monthly_rate) ** - month_duration)

    payment = amount*(monthly_rate/denominator)

    return payment, payment * month_duration - amount

def loan_monthly_table(amount: int, month_duration: int, yearly_rate: float) -> list[tuple[float, float, float, float]]:
    """
    :param amount: total amount of the load
    :param month_duration: duration in month of the credit
    :param yearly_rate: yearly interest rate betweeon 0 and 1 (not percent)
    """

    monthly_payment, _ = loan_total_cost_and_monthly_payment(amount, month_duration, yearly_rate)

    monthly_rate = yearly_rate / 12

    def _recursive_loan_monthly(balance: float, table: list) -> list[tuple[float, float, float, float]]:
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        if balance < 0:
            return table + [(0, monthly_payment, 0, amount)]
        return _recursive_loan_monthly(
            balance * (1 + monthly_rate) - monthly_payment,
            table + [(balance, principal, interest, amount - balance)]
        )

    return _recursive_loan_monthly(amount, [])

def dividend_investment_table(
    initial_deposit: int,
    dividend_yearly_increase: float,
    stock_expected_growth: float,
    dividend_yield: float,
    yearly_investiment: int,
    holding_duration: int,
    dividend_tax_rate: float,
    drip: bool
    ): 
    """
    :param initial_deposit: Initial deposit amount
    :param dividend_yearly_increase: Dividend year over year increase
    :param stock_expected_growth: Stock growth
    :param dividend_yield: Stock yearly returns as a dividend payment
    :param yearly_investiment: Total invested per year
    :param holding_duration_year: Total number of year to compute stats
    :param dividend_tax_rate: Yearly tax rate on "plus-value" returns
    :param drip: 
    """


    return end_balance, total_return, avg_yearly_return, yearly_dividend_income, total_dividend_payment, yield_on_cost