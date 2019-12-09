import pytest

from bankup.BankConnetors import BankConnectorBase


def test_givenABankConnectorBase_whenIwantToUseMethod_thenNotImplementedErrorIsRaised():
    '''
    GIVEN a BankConnectorBase
    WHEN I call the method 'fecth_balance'
    THEN an NotImplementedError is raised
    '''

    sut = BankConnectorBase()
    with pytest.raises(NotImplementedError):
        assert sut.fetch_balance()


def test_givenABankConnectorBase_whenIwantToUseTransactionsMethod_thenNotImplementedErrorIsRaised():
    '''
    GIVEN a BankConnectorBase
    WHEN I call the method 'fecth_transactions'
    THEN an NotImplementedError is raised
    '''

    sut = BankConnectorBase()
    with pytest.raises(NotImplementedError):
        assert sut.fetch_transactions()
