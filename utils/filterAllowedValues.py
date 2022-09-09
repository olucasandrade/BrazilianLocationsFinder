def exec(values, allowedValues=["name", "initials", "region", "cities"]):
    response = []
    for v in values:
        if v and str(v).lower() in allowedValues:
            response.append(v)
    return response