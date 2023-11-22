import re
import os

# コメント、空白行を削除し、[MESSAGES CONTROL]のみを出力
PATH = '/Users/tomoya-n/dev/2024_Noguchi/data/'
PATH_IN = PATH + 'pylintrc/gunicorn.txt'
PATH_OUTPUT = PATH + '/output/output.txt'
char_remove = '#'
title = '[MESSAGES CONTROL]'

with open(PATH_OUTPUT, 'w') as f:
    in_messages_control = False
    for line in open(PATH_IN, 'r'):
        if char_remove in line:
            continue
        if not line.strip():
            continue
        if title in line:
            in_messages_control = True
            continue
        if not in_messages_control:
            continue
        if  re.match(r'^\[\w', line):
            in_messages_control = False
            continue
        text = line.replace('\n', '')
        f.write(text.replace(' ', ''))

print('end')
