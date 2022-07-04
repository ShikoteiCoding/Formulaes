from formulas import loan_cost_and_payment, loan_monthly_table


if __name__ == "__main__":
    mensuality, cost = loan_cost_and_payment(100_000, 180, 0.01)
    table = loan_monthly_table(100_000, 180, 0.01)