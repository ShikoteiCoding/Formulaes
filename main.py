from formulas import loan_total_cost_and_monthly_payment, loan_monthly_table, dividend_investment_table

import pprint


if __name__ == "__main__":

    #mensuality, cost = loan_total_cost_and_monthly_payment(120_000, 120, 0.07)
    #table = loan_monthly_table(50_000, 180, 0.01)

    pp = pprint.PrettyPrinter(indent=4, width=200)

    result = dividend_investment_table(
        initial_capital=1_000,
        dividend_yield=0.05,
        dividend_annual_increase=0.02,
        position_expected_annual_growth=0.03,
        annual_contribution=12_000,
        holding_duration_year=4,
        dividend_tax_rate=0.3,
        drip=True
    )

    pp.pprint(result)