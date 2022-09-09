import json
from functools import reduce
from utils import getCitiesByState

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)

def getCities(obj):
    return obj['cities']

def exec(where):
    if where['state']:
        return getCitiesByState.exec(data, where['state'])
    arr = map(getCities, data)
    flatArr = reduce(lambda a,b:a+b, arr)
    return json.dumps(list(flatArr), ensure_ascii=False)