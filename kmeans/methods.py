def floatable(s):
    'Determine if an object can be converted to type float'
    try: float(s)
    except ValueError: return False
    return True
