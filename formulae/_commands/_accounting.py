from argparse import ArgumentParser
from typing import Any

from ._base import register


@register
def get_loan_total_cost_and_monthly_payment(args: Any) -> int:
    print("Executed")
    return 0


@register
def get_loan_monthly_table(args: Any) -> int:
    return 0
