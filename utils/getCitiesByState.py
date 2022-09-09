def exec(list, state):
    element = [item for item in list if item.get('initials').lower()==state.lower()]
    if (len(element)):
        return element[0].get('cities')
    return []
