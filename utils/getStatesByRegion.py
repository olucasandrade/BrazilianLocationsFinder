def getStatesByRegion(region):
    states = [item for item in list if item.get('region')==region.lower()]
    return states