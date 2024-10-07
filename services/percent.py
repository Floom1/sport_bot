def fat_percentage(gender, belly_girth, weight):
    if gender == 'male':
        fat = belly_girth * 0.74 - weight * 0.082 - 34.89
    else:
        fat = belly_girth * 0.74 - weight * 0.082 - 44.74

    return str(round(fat, 2))


def join(*args):
    return "".join(args)