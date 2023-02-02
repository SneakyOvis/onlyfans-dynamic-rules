import json
import sys
from account import Account

# Fill in the values.
cookies = ''
xbc = ''
userAgent = ''
#

account = Account(cookies, xbc, userAgent)
data = account.getMe()
print(json.dumps(data))
# data = account.getExpiredSubs()
# print(json.dumps(data))