## Banking
import numpy as np

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
        initial_capital: int,
        dividend_annual_increase: float,
        position_expected_annual_growth: float,
        dividend_yield: float,
        annual_contribution: int,
        holding_duration_year: int,
        dividend_tax_rate: float,
        drip: bool
    ): 
    """
    :param initial_capital: Initial deposit amount
    :param dividend_annual_increase: Dividend year over year increase
    :param position_expected_annual_growth: Stock growth
    :param dividend_yield: Stock yearly returns as a dividend payment
    :param annual_contribution: Total invested per year
    :param holding_duration_year: Total number of year to compute stats
    :param dividend_tax_rate: Yearly tax rate on "plus-value" returns
    :param drip: 
    """
    dtype = [
        ("year", np.int_), ("principal", np.float_), ("dividend", np.float_), ("yield", np.float_),
        ("principal_with_drip", np.float_), ("principal_increase", np.float_),
        ("annual_contribution", np.int_), ("new_balance", np.float_), ("cumulative_dividends", np.float_)
    ]

    def _recursive_one_year(year):

        if year == 1:
            annual_dividend = initial_capital * dividend_yield
            dividend_taxes = annual_dividend * dividend_tax_rate

            principal_after_drip = initial_capital + (annual_dividend  - dividend_taxes if drip else 0)
            principal_increase = initial_capital * position_expected_annual_growth
            new_balance = principal_after_drip + principal_increase + annual_contribution

            return np.array([(
                1, initial_capital, annual_dividend, dividend_yield * 100, principal_after_drip, principal_increase, annual_contribution, new_balance, annual_dividend
            )], dtype=dtype)
        

        table = _recursive_one_year(year - 1)
        prev = table[-1]

        annual_yield = (prev["yield"] / 100) * (1 + dividend_annual_increase - position_expected_annual_growth)
        annual_dividend = prev["new_balance"] * annual_yield
        dividend_taxes = annual_dividend * dividend_tax_rate

        principal_after_drip = prev["new_balance"] + (annual_dividend  - dividend_taxes if drip else 0)
        principal_increase = prev["new_balance"] * position_expected_annual_growth
        new_balance = principal_after_drip + principal_increase + annual_contribution

        return np.append(
                table, 
                np.array([(
                    prev["year"] + 1, prev["new_balance"], annual_dividend, annual_yield * 100, 
                    principal_after_drip, principal_increase, annual_contribution, new_balance, annual_dividend + prev["cumulative_dividends"]
                )], dtype=dtype)
            )

    return _recursive_one_year(holding_duration_year)