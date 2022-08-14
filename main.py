from formulas import (
    loan_total_cost_and_monthly_payment, loan_monthly_table, dividend_investment_table
)

import pprint
import pandas as pd
import numpy as np

def test_recursive():
    def _test(max):
        if max==0:
            return [max]
        else:
            prev_row =  _test(max - 1)
            print(prev_row)
            return prev_row + [max]

    print(_test(10))

def dividend_recursive():

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
    print(result)


if __name__ == "__main__":

    #mensuality, cost = loan_total_cost_and_monthly_payment(120_000, 120, 0.07)
    #table = loan_monthly_table(50_000, 180, 0.01)

    #rint(pd.DataFrame.from_records(result, index=["year"]))

    dividend_recursive()