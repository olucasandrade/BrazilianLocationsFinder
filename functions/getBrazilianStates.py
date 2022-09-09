from functools import partial
import json
from utils import filterValuesFromDict, getStatesByRegion

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)

def exec(where):
    response = data
    if where['region']:
        response = getStatesByRegion.exec(where['region'], response)
    if where['fields']:
        response = map(partial(filterValuesFromDict.exec, values=where['fields']), response)
    return json.dumps(list(response), ensure_ascii=False)