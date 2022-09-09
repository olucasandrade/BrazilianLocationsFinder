import json

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)

def exec(where):
    return json.dumps(data, ensure_ascii=False)