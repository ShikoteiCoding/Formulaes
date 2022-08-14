from accounting import (
    loan_total_cost_and_monthly_payment, loan_monthly_table, dividend_investment_table
)

import pprint
import pandas as pd
import numpy as np

def loan_table():
    result = loan_monthly_table(
        amount=100_000,
        month_duration=12,
        yearly_rate=0.02
    )
    print(pd.DataFrame.from_records(result, index=["month"]))

def dividend_table():

    result = dividend_investment_table(
        initial_capital=1_000,
        dividend_yield=0.05,
        dividend_annual_increase=0.02,
        position_expected_annual_growth=0.03,
        annual_contribution=12_000,
        holding_duration_year=40,
        dividend_tax_rate=0.3,
        drip=True
    )
    print(pd.DataFrame.from_records(result, index=["year"]))


if __name__ == "__main__":

    dividend_table()