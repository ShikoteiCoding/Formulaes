from argparse import ArgumentParser
from typing import Any

from ._base import register

from formulae.loan import loan_monthly_table, loan_total_cost_and_monthly_payment


@register
def get_loan_total_cost_and_monthly_payment(
    amount: int = 100000, month_duration: int = 12, yearly_rate: float = 0.05
) -> int:
    print(
        loan_total_cost_and_monthly_payment(
            amount=int(amount),
            month_duration=int(month_duration),
            yearly_rate=float(yearly_rate),
        )
    )
    return 0


@register
def get_loan_monthly_table(amount: int, month_duration: int, yearly_rate: float) -> int:
    print(
        loan_monthly_table(
            amount=int(amount),
            month_duration=int(month_duration),
            yearly_rate=float(yearly_rate),
        )
    )
    return 0
