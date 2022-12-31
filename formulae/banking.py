import numpy as np


#########################################
#####            Banking            #####
#########################################
def loan_total_cost_and_monthly_payment(
    amount: int, month_duration: int, yearly_rate: float
) -> tuple[float, float]:
    """
    :param amount: total amount of the load
    :param month_duration: duration in month of the credit
    :param yearly_rate: yearly interest rate betweeon 0 and 1 (not percent)
    """
    monthly_rate = yearly_rate / 12

    denominator = 1 - (1 + monthly_rate) ** -month_duration

    payment = amount * (monthly_rate / denominator)

    return payment, payment * month_duration - amount


def loan_monthly_table(amount: int, month_duration: int, yearly_rate: float):
    """
    :param amount: total amount of the load
    :param month_duration: duration in month of the credit
    :param yearly_rate: yearly interest rate betweeon 0 and 1 (not percent)
    """

    monthly_payment, _ = loan_total_cost_and_monthly_payment(
        amount, month_duration, yearly_rate
    )
    monthly_rate = yearly_rate / 12

    # Output table
    # :month: index of the table
    # :balance: start of month rest to pay
    # :principal: paid this month towards loan
    # :interest: paid this month towards interests
    # :end_balance: end of month rest to pay
    dtype = [
        ("month", np.int_),
        ("balance", np.float_),
        ("principal", np.float_),
        ("interest", np.float_),
        ("end_balance", np.float_),
        ("cumulative_interests", np.float_),
    ]

    def _recursive_loan_test(month):

        if month == 1:
            interest = amount * monthly_rate
            return np.array(
                [
                    (
                        month,
                        amount,
                        monthly_payment - interest,
                        interest,
                        amount - monthly_payment + interest,
                        interest,
                    )
                ],
                dtype=dtype,
            )

        table = _recursive_loan_test(month - 1)
        prev = table[-1]
        interest = prev["end_balance"] * monthly_rate

        # Remove epsilon end balance (successive roundings)
        end_balance = (
            0
            if prev["month"] == month_duration - 1
            else prev["end_balance"] - monthly_payment + interest
        )

        return np.append(
            table,
            np.array(
                [
                    (
                        prev["month"] + 1,
                        prev["end_balance"],
                        monthly_payment - interest,
                        interest,
                        end_balance,
                        prev["cumulative_interests"] + interest,
                    )
                ],
                dtype=dtype,
            ),
        )

    return _recursive_loan_test(month_duration)


#########################################
#####          Investment           #####
#########################################
def dividend_investment_table(
    initial_capital: int,
    dividend_annual_increase: float,
    position_expected_annual_growth: float,
    dividend_yield: float,
    annual_contribution: int,
    holding_duration_year: int,
    dividend_tax_rate: float,
    drip: bool,
):
    """
    :param initial_capital: Initial deposit amount
    :param dividend_annual_increase: Dividend year over year increase
    :param position_expected_annual_growth: Stock growth
    :param dividend_yield: Stock yearly returns as a dividend payment
    :param annual_contribution: Total invested per year
    :param holding_duration_year: Total number of year to compute stats
    :param dividend_tax_rate: Yearly tax rate on "plus-value" returns
    :param drip:
    """

    # Output table
    # :year: index of stats
    # :principal: flat capital
    # :dividend: earnings from principal yield
    # :yield: rate applied to compute dividend
    # :principal_with_drip: flat capital adjusted with taxed dividend earnings
    # :annual_contribution: flat capital added during the year
    # :end_balance: wallet value end of year
    # :cumulative_dividends: cumulative dividend earnings from composed principal yields
    dtype = [
        ("year", np.int_),
        ("principal", np.float_),
        ("dividend", np.float_),
        ("yield", np.float_),
        ("principal_with_drip", np.float_),
        ("principal_increase", np.float_),
        ("annual_contribution", np.int_),
        ("end_balance", np.float_),
        ("cumulative_dividends", np.float_),
    ]

    def _recursive_one_year(year):

        if year == 1:
            principal_after_drip = (
                initial_capital * (1 + dividend_yield * (1 - dividend_tax_rate))
                if drip
                else 1
            )

            return np.array(
                [
                    (
                        1,
                        initial_capital,
                        initial_capital * dividend_yield,
                        dividend_yield * 100,
                        principal_after_drip,
                        initial_capital * position_expected_annual_growth,
                        annual_contribution,
                        principal_after_drip
                        + initial_capital * position_expected_annual_growth
                        + annual_contribution,
                        initial_capital * dividend_yield,
                    )
                ],
                dtype=dtype,
            )

        table = _recursive_one_year(year - 1)
        prev = table[-1]

        annual_yield = (prev["yield"] / 100) * (
            1 + dividend_annual_increase - position_expected_annual_growth
        )
        principal_after_drip = (
            prev["end_balance"] * (1 + annual_yield * (1 - dividend_tax_rate))
            if drip
            else 1
        )

        return np.append(
            table,
            np.array(
                [
                    (
                        prev["year"] + 1,
                        prev["end_balance"],
                        prev["end_balance"] * annual_yield,
                        prev["yield"]
                        * (
                            1
                            + dividend_annual_increase
                            - position_expected_annual_growth
                        ),
                        principal_after_drip,
                        prev["end_balance"] * position_expected_annual_growth,
                        annual_contribution,
                        principal_after_drip
                        + prev["end_balance"] * position_expected_annual_growth
                        + annual_contribution,
                        prev["end_balance"] * annual_yield
                        + prev["cumulative_dividends"],
                    )
                ],
                dtype=dtype,
            ),
        )

    return _recursive_one_year(holding_duration_year)
