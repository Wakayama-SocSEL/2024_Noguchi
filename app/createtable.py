import pandas as pd
import os
from namelist import namelist

NUM_PROJECT=2
PROJECT_NAME_LIST = namelist.getProjectName(NUM_PROJECT)
NAME_ID_DICT = namelist.getNameIdDict()

V_NAME_LIST = list(NAME_ID_DICT.keys())
V_KEY_LIST = list(NAME_ID_DICT.values())
PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)) + '/data'
PATH_OUT = PATH + '/to_csv_out.csv'
TAG_D = 'disable'
TAG_I = 'disable-msg'
TAG_flag = ''

#集計用のリスト作成
count_id_dict = {}
for i in range(len(NAME_ID_DICT)):
    count_id_dict[V_KEY_LIST[i]] = 0


#ファイルから規約取得
def extract_violations_from_file(path, file_list):
    flag = ''
    with open(path, 'r') as f:
        for line in f:
            if TAG_I in line:
                flag = TAG_I
                continue
            if TAG_D in line:
                flag = TAG_D
                continue
            file_list.extend(line.split(','))
    return flag


#規約の比較
def compare_conventions(flag, input_list):
    output_dict = {}
    if flag == TAG_D:
        for i in range(len(NAME_ID_DICT)):
            for j in range(len(input_list)):
                if input_list[j] in V_NAME_LIST[i]:
                    output_dict[V_KEY_LIST[i]] = 'TRUE'
                    count_id_dict[V_KEY_LIST[i]] += 1
                    break
                output_dict[V_KEY_LIST[i]] = 'FALSE'

            continue
    if flag == TAG_I:
        for i in range(len(NAME_ID_DICT)):
            for j in range(len(input_list)):
                if input_list[j] in V_KEY_LIST[i]:
                    output_dict[V_KEY_LIST[i]] = 'TRUE'
                    count_id_dict[V_KEY_LIST[i]] += 1
                    break
                output_dict[V_KEY_LIST[i]] = 'FALSE'
    return output_dict

#表の作成
def createFrame(output_list):
    project_result_list = [output_list[i].values() for i in range(NUM_PROJECT)]
    df = pd.DataFrame(project_result_list)
    df.index = PROJECT_NAME_LIST
    df.columns = V_KEY_LIST
    df.to_csv(PATH_OUT)

#結果の取得
def getResultDict(num):
    exist_list = []
    judge_id_dict = {}
    path_in = PATH + '/output/' + PROJECT_NAME_LIST[num] + '_output.txt'
    TAG_flag = extract_violations_from_file(path_in, exist_list)
    judge_id_dict = compare_conventions(TAG_flag, exist_list)
    return judge_id_dict

#プロジェクト数分回す
result_list = []
for i in range(NUM_PROJECT):
    result_list.append(getResultDict(i))
createFrame(result_list)
    
print('end')