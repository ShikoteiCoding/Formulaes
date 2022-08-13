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
    :param initial_deposit: Initial deposit amount
    :param dividend_annual_increase: Dividend year over year increase
    :param position_expected_annual_growth: Stock growth
    :param dividend_yield: Stock yearly returns as a dividend payment
    :param yearly_investment: Total invested per year
    :param holding_duration_year: Total number of year to compute stats
    :param dividend_tax_rate: Yearly tax rate on "plus-value" returns
    :param drip: 
    """
    def _recursive_one_year(year, start_year_capital, start_year_yield, start_year_contribution, table):
        
        current_year_dividend = start_year_capital * start_year_yield
        current_year_taxes = current_year_dividend * dividend_tax_rate
        current_year_dividend_after_taxes = current_year_dividend  - current_year_taxes

        end_year_capital = start_year_capital * (1 + position_expected_annual_growth)
        end_year_dividend = current_year_dividend
        end_year_contribution = ((current_year_dividend_after_taxes if drip else 0) + start_year_contribution)
        end_year_balance = end_year_capital + end_year_contribution
        end_year_yield = start_year_yield * (1 + dividend_annual_increase - position_expected_annual_growth)
        
        if year == holding_duration_year:
            return table + [(year, start_year_capital, start_year_yield, start_year_capital, end_year_dividend, end_year_balance)]

        return _recursive_one_year(
            year + 1,
            end_year_balance,
            end_year_yield,
            end_year_contribution,
            table + [(year, start_year_capital, start_year_yield, start_year_capital, end_year_dividend, end_year_balance)]
        )

    return _recursive_one_year(1, initial_capital, dividend_yield, annual_contribution, [("Year", "Capital", "Yield", "Contribution", "Annual Dividend", "New Balance")])