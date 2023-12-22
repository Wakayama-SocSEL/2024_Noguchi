import os
import re
import sys
sys.path.append("../")

def extract_data(text):
    pattern = re.compile(r'^(.*?)(\([^)]*\)):')
    match = pattern.match(text)

    if match:
        key = match.group(1).strip()
        value = match.group(2).strip()
        return key, value
    else:
        return None, None

def process_strings(strings):
    result_dict = {}

    for text in strings:
        key, value = extract_data(text)
        if key in result_dict:
            continue
        if value in result_dict.values():
            continue
        if key:
            result_dict[key] = value

    return result_dict

def process_version_directory(version_directory):
    result_dict = {}

    for filename in os.listdir(version_directory):
        if filename.startswith("v_") and filename.endswith(".txt"):
            #print(filename)
            file_path = os.path.join(version_directory, filename)
            with open(file_path, 'r') as f:
                result = process_strings(f.readlines())
                result_dict.update(result)

    return result_dict

def save_to_file(data, output_path):
    with open(output_path, 'w') as f_out:
        for key, value in data.items():
            f_out.write(f"{key}: {value}\n")

# メインの処理
PATH =  sys.path[-1] + '/data/version'
version_directory = PATH
output_path = PATH + '/nameList.txt'

result = process_version_directory(version_directory)
save_to_file(result, output_path)

print('end')
