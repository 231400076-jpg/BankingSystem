import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

# ---------------- Deposit Tests ----------------

def test_deposit_positive_amount():
    assert deposit(1000, 500) == 1500

@pytest.mark.parametrize("balance, amount", [
    (1000, 0),
    (1000, -200)
])
def test_deposit_invalid_amount(balance, amount):
    with pytest.raises(ValueError):
        deposit(balance, amount)


# ---------------- Withdraw Tests ----------------

def test_withdraw_more_than_balance():
    with pytest.raises(ValueError):
        withdraw(500, 1000)


# ---------------- Transfer Tests ----------------

def test_transfer_success():
    from_balance, to_balance = transfer(1000, 500, 300)
    assert from_balance == 700
    assert to_balance == 800

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 500, 400)


# ---------------- Interest Tests ----------------

def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00
