from argparse import ArgumentParser
from typing import Any

from ._base import register
from formulae.investment import dividend_investment_table


@register
def get_dividend_investment_table(
    initial_capital: int,
    dividend_annual_increase: float,
    position_expected_annual_growth: float,
    dividend_yield: float,
    annual_contribution: int,
    holding_duration_year: int,
    dividend_tax_rate: float,
    drip: bool,
) -> int:
    print(
        dividend_investment_table(
            initial_capital=int(initial_capital),
            dividend_annual_increase=float(dividend_annual_increase),
            position_expected_annual_growth=float(position_expected_annual_growth),
            dividend_yield=float(dividend_yield),
            annual_contribution=int(annual_contribution),
            holding_duration_year=int(holding_duration_year),
            dividend_tax_rate=float(dividend_tax_rate),
            drip=bool(drip),
        )
    )
    return 0
