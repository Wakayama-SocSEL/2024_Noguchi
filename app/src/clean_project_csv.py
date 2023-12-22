import pandas as pd
import sys
sys.path.append("../")
from utils import clean_csv

PATH = sys.path[-1] + '/data'
PATH_IN = f'{PATH}/minami_output'
PATH_OUT = f'{PATH}/processed/csv'

clean_csv.delete_rows(PATH_IN, PATH_OUT, 0, 0)
clean_csv.delete_columns(PATH_OUT, PATH_OUT, 0, 3)
print('end')

