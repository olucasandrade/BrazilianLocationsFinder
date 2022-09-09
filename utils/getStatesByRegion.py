def exec(region, list):
    states = [item for item in list if item.get('region').lower()==region.lower()]
    return states