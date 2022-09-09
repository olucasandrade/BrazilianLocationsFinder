from . import filterAllowedValues

def exec(dict, values):
    result = {}
    allowedValues = filterAllowedValues.exec(values)
    for v in allowedValues:
        result[v] = dict[v]
    return result
