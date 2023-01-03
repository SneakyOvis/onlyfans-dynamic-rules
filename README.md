# Where are the rules

`https://raw.githubusercontent.com/SneakyOvis/onlyfans-dynamic-rules/main/rules.json`

You can find the documentation in the **doc** directory

# How to generate **sign** header from rules:

```javascript
import sha1 from 'js-sha1';

const rules = JSON.parse(`{
    "app-token": "33d57ade8c02dbc5a333db99ff9ae26a",
    "static_param": "n4GYH4LDIHQzGeLh2oxRhjaQdl1yNsg8",
    "prefix": "6471",
    "suffix": "63b430f2",
    "checksum_constant": 544,
    "checksum_indexes": [0,0,0,1,2,2,5,7,8,9,12,12,12,16,19,19,21,22,23,24,24,25,26,27,29,30,31,31,32,33,33,36]
}`);
const path = '/api/path';
const time = Date.now().toString();
const hash = sha1([rules['static_param'], time, path, rules['user-id']].join('\n'));
const checksum = rules['checksum_indexes'].reduce((total, current) => total += hash[current].charCodeAt(0), 0) + rules['checksum_constant'];
const sign = [rules['prefix'], hash, checksum.toString(16), rules['suffix']].join(':');
console.log(sign);
```

# How to make api request:

```javascript
import sha1 from 'js-sha1';

const rules = JSON.parse(`{
    "app-token": "33d57ade8c02dbc5a333db99ff9ae26a",
    "static_param": "n4GYH4LDIHQzGeLh2oxRhjaQdl1yNsg8",
    "prefix": "6471",
    "suffix": "63b430f2",
    "checksum_constant": 544,
    "checksum_indexes": [0,0,0,1,2,2,5,7,8,9,12,12,12,16,19,19,21,22,23,24,24,25,26,27,29,30,31,31,32,33,33,36]
}`);

function createHeaders(path, rules) {
    const time = Date.now().toString();
    const hash = sha1([rules['static_param'], time, path, rules['user-id']].join('\n'));
    const checksum = rules['checksum_indexes'].reduce((total, current) => total += hash[current].charCodeAt(0), 0) + rules['checksum_constant'];
    const sign = [rules['prefix'], hash, checksum.toString(16), rules['suffix']].join(':');
    return {
        accept: 'application/json, text/plain, */*',
        'app-token': rules['app-token'],
        cookie: rules['cookie'],
        sign: sign,
        time: time,
        'user-id': rules['user-id'],
        'user-agent': rules['user-agent'],
        'x-bc': rules['x-bc']
    };
}

async function callAPI(path, rules) {
    rules = {
        ...rules,
        ...{
            'user-id': 'get from browser',
            'x-bc': 'get from browser',
            'cookie': 'get from browser',
            'user-agent': 'get from browser'
        }
    };

    const headers = createHeaders(path, rules);
    const response = await fetch(
        `https://onlyfans.com${path}`,
        { headers: headers }
    );
    
    return await response.json();
}

const path = '/api2/v2/users/list?r2[]=255449830';
const data = await callAPI(path, rules);
console.log(data);
```
