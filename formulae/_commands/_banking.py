from argparse import ArgumentParser
from typing import Any

from ._base import register

from formulae.banking import loan_monthly_table, loan_total_cost_and_monthly_payment, dividend_investment_table


@register
def get_loan_total_cost_and_monthly_payment(
    amount: int=100000, month_duration: int=12, yearly_rate: float=0.05
    ) -> int:
    print(loan_total_cost_and_monthly_payment(amount=int(amount), month_duration=int(month_duration), yearly_rate=float(yearly_rate)))
    return 0


@register
def get_loan_monthly_table(amount: int, month_duration: int, yearly_rate: float) -> int:
    print(loan_monthly_table(amount=int(amount), month_duration=int(month_duration), yearly_rate=float(yearly_rate)))
    return 0

@register
def get_dividend_investment_table(
    initial_capital: int,
    dividend_annual_increase: float,
    position_expected_annual_growth: float,
    dividend_yield: float,
    annual_contribution: int,
    holding_duration_year: int,
    dividend_tax_rate: float,
    drip: bool) -> int:
    print(
        dividend_investment_table(
            int(initial_capital),
            float(dividend_annual_increase),
            float(position_expected_annual_growth),
            float(dividend_yield),
            int(annual_contribution),
            int(holding_duration_year),
            float(dividend_tax_rate),
            bool(drip)
    ))
    return 0