from functools import partial
import json
from utils import filterValuesFromDict, getStatesByRegion, orderBy

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)

def exec(where):
    response = data
    if where.get('orderBy'):
        response = orderBy.exec(response, where.get('orderBy'))
    if where.get('region'):
        response = getStatesByRegion.exec(where.get('region'), response)
    if where.get('fields'):
        response = map(partial(filterValuesFromDict.exec, values=where.get('fields')), response)
    return json.dumps(list(response), ensure_ascii=False)