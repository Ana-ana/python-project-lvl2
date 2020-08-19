DICTIONARY_FROM_BEFORE = {"host": "hexlet.io",
                          "timeout": 50,
                          "proxy": "123.234.53.22"}

DICTIONARY_FROM_AFTER = {"timeout": 20,
                         "verbose": True,
                         "host": "hexlet.io"}

DICTIONARY_FINAL_DIFFERENCE = {'  host': 'hexlet.io',
                               '- timeout': 50,
                               '+ timeout': 20,
                               '+ verbose': True,
                               '- proxy': '123.234.53.22'}

DICTIONARY_LIST_OF_DIFFERENCES = {'common': {'host': 'hexlet.io'},
                                  'changed': {'timeout': [20, 50]},
                                  'added': {'verbose': True},
                                  'removed': {'proxy': '123.234.53.22'}}
