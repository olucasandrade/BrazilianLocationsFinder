def exec(list, key):
    return sorted(list, key=lambda obj: obj[key])
