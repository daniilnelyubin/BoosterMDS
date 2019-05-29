def update_dictionary(d, key, value):
    if key not in d.keys():
        if 2*key not in d.keys():
            d[2 * key] = [value]
        else:
            d[2 * key].append(value)
    else:
        d[key].append(value)
            
