import pytest

from bankup.Bankup import Bankup


class FakeBankConnector(object):
    def __init__(self):
        self._balance = 12
        self._transactions = [
            {"date": "2019-11-02 ",
            "amount": 34.2,
            },
            {"date": "2019-11-02 ",
            "amount": 34.2,
            },
            {"date": "2019-11-02 ",
            "amount": 34.2,
            }
        ]

    def fetch_transactions(self, since=""):
        return self._transactions

    def fetch_balance(self):
        return self._balance

@pytest.fixture(scope='module')
def fake_bank_connector():
    fake_bank_connector = FakeBankConnector()
    return fake_bank_connector


def test_givenABankupWithABankConnector_whenFetchBalance_thenReturnBalanceFromConnector(
    fake_bank_connector
):

    sut = Bankup(bank_connector=fake_bank_connector)
    assert sut.fetch_balance() == 12

def test_givenABankupWithConnector_whenAskTransactionsFromDate_then(
    fake_bank_connector
):
    '''
    GIVEN Bankup with a BankConnector
    WHEN I ask the transactions from a date
    THEN return the list of all transactions
    '''
    sut = Bankup(bank_connector=fake_bank_connector)

    transactions = sut.fetch_transactions(since="2019-11-01")
    assert len(transactions) == 3

