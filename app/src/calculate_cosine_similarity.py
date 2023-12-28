import numpy as np
import pandas as pd
import csv
import sys
sys.path.append("../")
from utils import get_file_name

PATH = f'{sys.path[-1]}/data/'
PATH_IN = f'{PATH}/out/tracking_test_convention.csv'
PATH_OUT = f'{PATH}/out/cos_sim.csv'
PROJECT_NAME_LIST = get_file_name(f'{PATH}/test')
PROJECT_NUM = len(PROJECT_NAME_LIST)

#コサイン類似度の測定
def cos_sim(v1, v2):
    # Noneを1000として取り出す
    v1_numeric = [float(x) if x and x != 'None' else 1000 for x in v1[1:]]
    v2_numeric = [float(x) if x and x != 'None' else 1000 for x in v2[1:]]
    
    return np.dot(v1_numeric, v2_numeric) / \
           (np.linalg.norm(v1_numeric) * np.linalg.norm(v2_numeric))

# 表の作成
def createFrame(output_list):
    df = pd.DataFrame(output_list)
    df.index = PROJECT_NAME_LIST
    df.columns = PROJECT_NAME_LIST
    df.to_csv(PATH_OUT)

#csvファイルから規約ごとの修正率の収集
project_correction_rates = [[] for i in range(PROJECT_NUM)] 
with open(PATH_IN, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        for num in range(1, PROJECT_NUM + 1):
            project_correction_rates[num - 1].append(row[num])

result_list = [[] for i in range(PROJECT_NUM)]   
for i in range(5):
    for j in range(5): 
        result_list[i].append(round(cos_sim(project_correction_rates[i], project_correction_rates[j]), 2))   
createFrame(result_list)
print('end')
