import hashlib
import requests
import sys
import time

DEBUG = False
SLEEP = .01

# code from https://github.com/psf/requests/issues/6115
import urllib3.util.url as urllib3_url

def hook_invalid_chars(component, allowed_chars):
    # handle url encode here, or do nothing
    return component

urllib3_url._encode_invalid_chars = hook_invalid_chars
#

class AccountBase:
    def __init__(self, cookies, xbc, userAgent):
        self.cookies = cookies
        self.xbc = xbc
        self.userAgent = userAgent
        self.userID = self.getUserID()
        self.session = requests.Session()

        rules = requests.get('https://raw.githubusercontent.com/SneakyOvis/onlyfans-dynamic-rules/main/rules.json').json()
        self.appToken = rules['app-token']
        self.signStaticParam = rules['static_param']
        self.signChecksumConstant = rules['checksum_constant']
        self.signChecksumIndexes = rules['checksum_indexes']
        self.signPrefix = rules['prefix']
        self.signSuffix = rules['suffix']

    def getUserID(self):
        for cookie in self.cookies.split(';'):
            name, value = cookie.strip().split('=')
            if name == 'auth_id':
                return value
        
        return ''

    def createHeaders(self, path):
        timestamp = str(int(time.time() * 1000))
        sha = hashlib.sha1('\n'.join([self.signStaticParam, timestamp, path, self.userID]).encode('utf-8')).hexdigest()
        checksum = sum(ord(sha[n]) for n in self.signChecksumIndexes) + self.signChecksumConstant
        sign = ':'.join([self.signPrefix, sha, '%x' % checksum, self.signSuffix])
        return {
            'accept': 'application/json, text/plain, */*',
            'app-token': self.appToken,
            'cookie': self.cookies,
            'sign': sign,
            'time': timestamp,
            'user-id': self.userID,
            'user-agent': self.userAgent,
            'x-bc': self.xbc
        }

    def get(self, path):
        time.sleep(SLEEP)
        headers = self.createHeaders(path)
        response = self.session.get(f'https://onlyfans.com{path}', headers=headers)
        if DEBUG:
            print(f'--get {response.request.url}', file=sys.stderr)

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error: {response.status_code}, response text: {response.text}', file=sys.stderr)
            return None
