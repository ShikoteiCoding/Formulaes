from formulas import loan_total_cost_and_monthly_payment, loan_monthly_table

import math


if __name__ == "__main__":

    mensuality, cost = loan_total_cost_and_monthly_payment(120_000, 120, 0.07)
    table = loan_monthly_table(50_000, 180, 0.01)
    
    print(mensuality, cost)