import re
import os

# コメント、空白行を削除し、[MESSAGES CONTROL]の中身のみを出力
project_name = 'boto'
PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)) + '/data'
PATH_IN = PATH + '/pylintrc/' + project_name + '.txt'
PATH_OUTPUT = PATH + '/output/' + project_name + '_output.txt'
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
    f.write('\n')

print('end')
