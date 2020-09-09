from collections import defaultdict

COMMON = 'common'
CHANGED = 'changed'
ADDED = 'added'
REMOVED = 'removed'
NESTED = 'nested'

INDENT = {
    'added': '+ ',
    'removed': '- ',
    'common': '  ',
    'changed': '',
    'nested': ''
}


def generate_diff(before, after):
    difference = defaultdict(dict)
    for key in before.keys() & after.keys():
        if isinstance(before[key], dict) and isinstance(after[key], dict):
            difference[NESTED][key] = generate_diff(before[key], after[key])
        elif before[key] == after[key]:
            difference[COMMON][key] = before[key]
        else:
            difference[CHANGED][key] = [after[key], before[key]]
    for key in after.keys() - before.keys():
        difference[ADDED][key] = after[key]
    for key in before.keys() - after.keys():
        difference[REMOVED][key] = before[key]
    return difference
