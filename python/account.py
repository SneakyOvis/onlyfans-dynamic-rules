import json
from os import path
import sys

from account_base import AccountBase

class Account(AccountBase):
    def getMe(self):
        return self.get(f'/api2/v2/users/me')

    def getExpiredSubs(self):
        offset = 0
        subs = []
        while True:
            data = self.get(f'/api2/v2/subscriptions/subscribers?limit=10&offset={offset}&sort=desc&field=last_activity&type=expired')
            if not data:
                break

            subs.extend(data)
            offset += 10
            if len(data) == 0 or len(data) < 10:
                break

        return subs