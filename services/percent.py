def fat_percentage(gender, belly_girth, high, weight):
    if gender == 'male':
        fat = 0.31457 * belly_girth - 0.10969 * weight + 10.834
    else:
        fat = 0.11077 * belly_girth - 0.17666 * high + 0.14354 * weight + 51.033

    return fat
