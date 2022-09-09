from functools import partial
import json
from utils import filterValuesFromDict

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)

def exec(where):
    response = data
    if where['fields']:
        response = map(partial(filterValuesFromDict.exec, values=where['fields']), response)
    return json.dumps(list(response), ensure_ascii=False)