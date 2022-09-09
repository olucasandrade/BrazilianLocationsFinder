def exec(values):
    response = []
    allowedValues = ["name", "initials", "region", "cities"]
    for v in values:
        if v and str(v).lower() in allowedValues:
            response.append(v)
    return response