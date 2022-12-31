import numpy as np


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
