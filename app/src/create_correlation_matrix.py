import numpy as np
import pandas as pd
import sys
sys.path.append("../")
from utils import calculate_cosin_similarity
from utils import load_correction_data
PATH = f'{sys.path[-1]}/data/'

PATH_IN = f'{PATH}/out/cleaned_tracking_all_convention.csv'
PATH_OUT = f'{PATH}/out/test_all_cos_sim.csv'
PATH_OUT_SORTED = f'{PATH}/out/test_sort_cosine.csv'

#test
# PATH_IN = f'{PATH}/out/tracking_test_convention.csv'
# PATH_OUT = f'{PATH}/out/cos_sim.csv'
# PROJECT_NAME_LIST = get_file_name(f'{PATH}/test')

# 表の作成
def createFrame(output_list, path, project_names):
    df = pd.DataFrame(output_list)
    df.index = project_names
    df.columns = project_names
    df.to_csv(path)

PROJECT_NAME_LIST = load_correction_data.get_project_name(PATH_IN)
project_correction_rates = load_correction_data.correction_from_csv(PATH_IN)
PROJECT_NUM = len(PROJECT_NAME_LIST)

#コサイン類似度の計算
result_list = [[] for _ in range(PROJECT_NUM)]   
for i in range(PROJECT_NUM):
    for j in range(PROJECT_NUM):
        result_cosin = calculate_cosin_similarity.cos_sim(project_correction_rates[i], project_correction_rates[j])
        result_list[i].append(round(result_cosin[0], 3))

# 表の作成
createFrame(result_list, PATH_OUT, PROJECT_NAME_LIST)

#組み合わせの表示
project_combinations_list = []
count_list = []
for i in range(PROJECT_NUM):
    for j in range(i, PROJECT_NUM):
        result_combinations = cos_sim(project_correction_rates[i], project_correction_rates[j])
        project_combinations_list.append(result_combinations[0])
        count_list.append(result_combinations[1])

#データフレームの作成
        
# sample = [['1.0', '0.86', '1.0', '1.0', '0.14', '0.86', '1.0', '1.0', '0.57', '1.0', '0.0', '1.0', '0.15', '1.0', '1.0', '1.0', '0.0', '1.0', '0.0', '0.0', '0.0', '1.0', '0.0', '1.0', '1.0', '0.75', '0.8', '0.0', '0.33', '0.33', '0.33', '0.33', '0.0', '1.0', '0.0', '1.0', '0.29', '0.85', '0.4', '0.0', '0.0', '0.75', '0.17', '0.0', '0.33', '0.0', '1.0', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],\
#             ['None', 'None', 'None', 'None', '1.0', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '0.0', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '1.0', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']]
# print(cos_sim(sample[0], sample[1]))




# # コサイン類似度を1次元のリストに平坦化
# flat_result_list = [similarity for sublist in result_list for similarity in sublist]

# # ソート
# sorted_result_list = sorted(enumerate(flat_result_list), key=lambda x: x[1], reverse=True)

# # 表示用のデータフレーム作成
# display_df = pd.DataFrame(columns=['Project 1', 'Project 2', 'Similarity', 'Count'])

# # 既に表示した組み合わせを保持するためのセット
# displayed_combinations = set()

# for i, (index, similarity) in enumerate(sorted_result_list):
#     project_name1 = PROJECT_NAME_LIST[index // PROJECT_NUM]
#     project_name2 = PROJECT_NAME_LIST[index % PROJECT_NUM]

#     # Project 1 と Project 2 の順序を入れ替えても同じ組み合わせとみなす
#     combination = frozenset([project_name1, project_name2])

#     if similarity < 1 and combination not in displayed_combinations:
#         display_df = pd.concat([display_df, pd.DataFrame({'Project 1': [project_name1], 'Project 2': [project_name2], 'Similarity': [similarity]})], ignore_index=True)
#         displayed_combinations.add(combination)

# データフレームを表示
print(display_df)
display_df.to_csv(PATH_OUT_SORTED, index = False)

