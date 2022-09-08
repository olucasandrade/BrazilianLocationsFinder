def filterValuesFromDict(dict, values):
    result = {}
    for v in values:
        result[v] = dict[v]
    return result
