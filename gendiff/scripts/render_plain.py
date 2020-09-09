from gendiff.scripts.generate_difference import *


def render_plain(diff_obj):
    rendered_str = []
    for diff_key in sorted(diff_obj.keys()):
        for k, v in diff_obj[diff_key].items():
            if diff_key == NESTED:
                for _ in render_plain(v):
                    rendered_str.append('{}.{}'.format(k, _))
            else:
                if diff_key == ADDED:
                    rendered_str.append('{} was added with value {}'.format(k, replace_dict(v)))
                if diff_key == REMOVED:
                    rendered_str.append('{} was removed'.format(k))
                if diff_key == CHANGED:
                    rendered_str.append('{} was updated from {} to {}.'.format(k, replace_dict(v[1]), replace_dict(v[0])))

    return format_plain_text(rendered_str)


def replace_dict(itm):
    if isinstance(itm, dict):
        itm = '[complex value]'
    return itm


def format_plain_text(rendered_list):
    output = []
    for item in rendered_list:
        output.append('Property ' + item)
    return output

