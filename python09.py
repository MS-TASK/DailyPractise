from datetime import date
import json

print(date.today())

data = {
    'code': '001',
    'name':'No.1'
}

json_str = json.dumps(data)

print(repr(data))
print(json_str)


