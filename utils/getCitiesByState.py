def getCitiesByState(list, state):
    element = [item for item in list if item.get('state').lower()==state.lower()]
    return element[0].get('cities')
