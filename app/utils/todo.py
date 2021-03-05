def quantity_tasks(dicts):
    result = {}
    for key, value in dicts.items():
        if value is not None:
            result[key] = len(value)
        else:
            result[key] = '0'
    return result
