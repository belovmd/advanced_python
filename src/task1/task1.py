"""Advanced Python courses. Homework#7, Task #1.Maxim Belov.

Implementation of wallet class.
"""

import json
import requests


class Wallet(object):
    """Class represents simple wallet model."""

    tmpl = '{url}?access_key={token}&source={source}&currencies={currency}'
    url = 'http://www.apilayer.net/api/live'
    token = "a3e9c4a8282827fa2ea47bddc89bb27c"
    default_source = 'USD'

    def __init__(self, start_value, currency='USD'):
        self.currency = currency.upper()
        self.balance = start_value

    def __str__(self):
        return ('{balance:.2f} {currency}'.format(balance=self.balance,
                                                  currency=self.currency))

    def __mul__(self, other):
        return Wallet(self.balance * other, self.currency)

    def __imul__(self, other):
        self.balance *= other
        return self

    def __rmul__(self, other):
        return self * other

    def __iadd__(self, other):
        self.balance += other.balance * self._get_rate(other.currency)
        return self

    def __radd__(self, other):
        return self + other

    def __add__(self, other):
        try:
            exchanged_value = other.balance * self._get_rate(other.currency)
            balance = self.balance + exchanged_value
        except Exception:
            return self
        else:
            return Wallet(balance, self.currency)

    def _get_rate(self, currency):
        """Count wallet currency to currency rate."""
        request_currencies = ','.join((self.currency, currency))
        response = requests.get(self.tmpl.format(url=self.url,
                                                 token=self.token,
                                                 source=self.default_source,
                                                 currency=request_currencies))
        # our service doesn't support source currency change for free accounts
        currency_pair = self.default_source + currency
        wallet_pair = self.default_source + self.currency
        try:
            wallet_rate = json.loads(response.text)["quotes"][wallet_pair]
            currency_rate = json.loads(response.text)["quotes"][currency_pair]
        except Exception:
            return
        else:
            return wallet_rate / currency_rate


if __name__ == '__main__':

    a = Wallet(15.37, 'byn')
    b = Wallet(10, 'usd')
    c = Wallet(8, 'eur')
    print(a, b, c)
    a += b
    c *= 3
    print(a, b, c)
    lst = [a, b, c]
    print(sum(lst))
    print(c + 0.1 * b + a * 2)
