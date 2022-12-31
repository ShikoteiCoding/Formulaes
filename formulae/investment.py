import numpy as np


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
