import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest, check_loan_eligibility

# ---------------- Deposit White-Box ----------------

def test_deposit_error_branch():
    with pytest.raises(ValueError):
        deposit(1000, -100)


# ---------------- Withdraw White-Box ----------------

def test_withdraw_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -50)

def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 1000)

def test_withdraw_success_branch():
    assert withdraw(1000, 200) == 800


# ---------------- Transfer White-Box ----------------

def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -100)

def test_transfer_insufficient_balance_branch():
    with pytest.raises(ValueError):
        transfer(300, 500, 600)

def test_transfer_success_branch():
    from_balance, to_balance = transfer(1000, 500, 400)
    assert from_balance == 600
    assert to_balance == 900


# ---------------- Interest White-Box ----------------

def test_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 2)

def test_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)

def test_interest_success_branch():
    assert round(calculate_interest(1000, 10, 1), 2) == 1100.00


# ---------------- Loan Eligibility White-Box ----------------

def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True

def test_loan_not_eligible():
    assert check_loan_eligibility(3000, 650) is False
