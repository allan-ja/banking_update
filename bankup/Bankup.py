class Bankup(object):

    def __init__(self, bank_connector=None):
        self._bank_connector = bank_connector


    def fetch_balance(self):
        return self._bank_connector.fetch_balance()

    def fetch_transactions(self, since=""):
        return self._bank_connector.fetch_transactions(since=since)
