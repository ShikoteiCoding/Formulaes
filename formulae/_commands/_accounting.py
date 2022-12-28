from argparse import ArgumentParser

from ._base import register

@register
def get_loan_total_cost_and_monthly_payment() -> int:
    return 0

@register
def get_loan_monthly_table() -> int:
    return 0