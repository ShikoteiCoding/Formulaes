# Formulaes

# Description
Store the formula important to know but always forgotten.

The CLI is dynamic, is that a good idea ? Not sure as it bounds tightly the function signatures to the cli arguments.

# Run

## As a package

Run the demo
```shell
python3 demo.py
```

## As a CLI

Run one command
```shell
python3 -m formulae get_loan_total_cost_and_monthly_payment 
```

Example commands
```shell
python3 -m formulae get_dividend_investment_table \
    --initial_capital 3000 \
    --dividend_annual_increase 0.00 \
    --position_expected_annual_growth 0.00 \
    --dividend_yield 0.07 \
    --annual_contribution 36000 \
    --holding_duration_year 30 \
    --dividend_tax_rate 0 \
    --drip False
```