import pandas as pd
import os
import sys
import csv
sys.path.append("../")
from utils import get_file_name
from utils import tracking_convention
from utils import compare_convention

PATH = f'{sys.path[-1]}/data'
PATH_IN = f'{PATH}/processed/csv'
#PATH_IN = f'{PATH}/test'
PATH_OUT = f'{PATH}/out/tracking_all_convention.csv'
PROJECT_NAME_LIST = get_file_name(PATH_IN)

coding_convention_list = []
all_list = []
result_list = []
#print(tracking_convention(f'{PATH_IN}/analytics-python.csv'))
# coding_convention_dist = tracking_convention(f'{PATH_IN}/analytics-python.csv')
                    
# compare_convention(f'{PATH_IN}/analytics-python.csv', coding_convention_dist)
# for key, value in coding_convention_dist.items():
#     if value[1] == 0:
#         continue
#     coding_convention_dist[key] = round(value[0] / value[1], 2)
# print(coding_convention_dist)


# ディレクトリ内のすべてのファイルに対して実行
files = os.listdir(PATH_IN)
for file in sorted(files, key=lambda x: x.lower()):
    full_path = f'{PATH_IN}/{file}'
    print(full_path)
    coding_convention_dist = tracking_convention(full_path)
    coding_convention_dist = compare_convention(full_path, coding_convention_dist)
    
    #すべてのコーディング規約の取得
    for coding_convention in coding_convention_dist.keys():
        if  coding_convention not in  coding_convention_list:
            coding_convention_list.append(coding_convention)

    #coding_convention_distの値をパーセントに変更
    for key, value in coding_convention_dist.items():
        if value[1] == 0:
            continue
        coding_convention_dist[key] = round(value[0] / value[1], 2)

    result_list.append(coding_convention_dist)

# すべての規約には存在するが、各プロジェクトごとに存在しない規約の値をNoneにする
coding_convention_list.sort()
for i in range(len(result_list)):
    for j in coding_convention_list:
        result_list[i].setdefault(j, 'None')

# DataFrameの作成とCSVへの保存
df = pd.DataFrame({PROJECT_NAME_LIST[i]: result_list[i] for i in range(len(result_list))})
df.to_csv(PATH_OUT)
