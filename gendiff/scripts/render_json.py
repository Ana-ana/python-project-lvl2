from gendiff.scripts.generate_difference import *


def render_json(diff_obj, indent=' '):
    rendered_diff = ['{']
    for diff_key in sorted(diff_obj.keys()):
        for diff_obj_key, diff_obj_value in diff_obj[diff_key].items():
            if diff_key == NESTED:
                rendered_diff.append(
                    format_output(INDENT[diff_key], diff_obj_key, render_json(diff_obj_value, indent + ' ' * 2), indent))  # noqa: E501
            elif isinstance(diff_obj_value, dict):
                rendered_diff.append(format_output(
                    INDENT[diff_key], diff_obj_key, render_json({COMMON: diff_obj_value}, indent + ' ' * 2), indent))  # noqa: E501
            else:
                if diff_key == COMMON:
                    rendered_diff.append(format_output(INDENT[COMMON], diff_obj_key, diff_obj_value, indent))  # noqa: E501
                elif diff_key == CHANGED:
                    rendered_diff.append(format_output(INDENT[REMOVED], diff_obj_key, diff_obj_value[1], indent))  # noqa: E501
                    rendered_diff.append(format_output(INDENT[ADDED], diff_obj_key, diff_obj_value[0], indent))  # noqa: E501
                elif diff_key == ADDED:
                    rendered_diff.append(format_output(INDENT[ADDED], diff_obj_key, diff_obj_value, indent))  # noqa: E501
                elif diff_key == REMOVED:
                    rendered_diff.append(format_output(INDENT[REMOVED], diff_obj_key, diff_obj_value, indent))  # noqa: E501
    rendered_diff.append(indent + '}')
    return '\n'.join(rendered_diff)


def format_output(action_key, dic_key, dic_value, indent):
    if isinstance(dic_value, dict):
        rendered_dict = ['{']
        for key, value in dic_value.items():
            rendered_dict.append('{}{}: {}'.format(indent * 4, key, value))
        rendered_dict.append(indent * 2 + '}')
        return '{}{}{}: {}'.format(indent, action_key, dic_key, '\n'.join(rendered_dict))  # noqa: E501
    else:
        return '{}{}{}: {}'.format(indent, action_key, dic_key, dic_value)
