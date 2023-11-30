import pandas as pd


def createFrame(num):
    list1 = [num, num + 1, num + 2]
    df = pd.DataFrame(list1)
    df.index([num])
    df.columns('1', '2', '3')
    return df

print(createFrame(2))