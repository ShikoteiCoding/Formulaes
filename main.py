from formulas import loan_cost_and_payment


if __name__ == "__main__":
    mensuality, cost = loan_cost_and_payment(100_000, 180, 0.01)
    print(mensuality)
    print(cost)
    #print(principal)
    #print(interests)