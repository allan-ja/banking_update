class BankConnectorBase():

    def fetch_transactions(self):
        raise NotImplementedError

    def fetch_balance(self):
        raise NotImplementedError
