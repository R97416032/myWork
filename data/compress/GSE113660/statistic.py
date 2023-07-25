import pandas as pd


def statistic(path):
    data=pd.read_csv(path)
    type=data["gene_type"].values
    type=set(type)
    type=[*type]
    type.sort()
    print(type)
    count=[]
    sample=data.columns[3:].values
    for t in type:
        num=0
        for s in sample:
            num=num+sum(data[data["gene_type"]==t][s].values)
        count.append(num)
    print(type)
    print(count)
path="GSE113660.csv"
statistic(path)