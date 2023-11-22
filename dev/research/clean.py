import re
import os

# コメント、空白行を削除し、[MESSAGES CONTROL]のみを出力
PATH = '/Users/tomoya-n/dev/pylintrc/gunicorn.txt'
PATH_OUTPUT = '/Users/tomoya-n/dev/output/output.txt'
char_remove = '#'
title = '[MESSAGES CONTROL]'

with open(PATH_OUTPUT, 'w') as f:
    in_messages_control = False
    for line in open(PATH, 'r'):
        if title in line:
            in_messages_control = True
        elif in_messages_control and re.match(r'^\[\w', line):
            in_messages_control = False
        if in_messages_control and char_remove not in line and line.strip() and title in line:
            text = line.replace('\n', '')
            f.write(text.replace(' ', ''))

print('end')
