import pandas as pd
from scipy.io import mmread


def mtx2csv(barcodes_path,genes_path,matrix_path,genecode_path):
    barcodes=pd.read_table(barcodes_path,header=None)
    samples=barcodes[0].values
    genes=pd.read_table(genes_path,sep='\t',index_col=None,header=None)
    geneid=genes[0].values
    genename=genes[1].values
    genetype=[]
    genecode=pd.read_csv(genecode_path)
    for gid,gname in zip(geneid,genename):
        if len(genecode[genecode["gene_id"]==gid]["gene_type"].values)>0:
            genetype.append(genecode[genecode["gene_id"]==gid]["gene_type"].values[0])
        elif len(genecode[genecode["gene_name"]==gname]["gene_type"].values)>0:
            genetype.append(genecode[genecode["gene_name"]==gname]["gene_type"].values[0])
        else:
            genetype.append("unknow")

    columns=["geneid","genename","genetype",*barcodes[0].values]
    df=pd.DataFrame(columns=columns)
    df["geneid"]=geneid
    df["genename"]=genename
    df["genetype"]=genetype
    Matrix = (mmread(matrix_path))
    B = Matrix.todense()
    df = pd.DataFrame(B,columns=samples)
    df.insert(0,"gene_type",genetype)
    df.insert(0,"gene_name",genename)
    df.insert(0,"gene_id",geneid)
    df.to_csv(barcodes_path.split("_")[0]+".csv",index=None)

barcodes_path="../data/compress/GSE113660/GSE113660_RAW/ungz/GSM3110765_barcodes.tsv"
genes_path="../data/compress/GSE113660/GSE113660_RAW/ungz/GSM3110765_genes.tsv"
matrix_path="../data/compress/GSE113660/GSE113660_RAW/ungz/GSM3110765_matrix.mtx"
genecode_path="../data/genecode/v43/all/ungz/gencode.v43.annotation.csv"

mtx2csv(barcodes_path,genes_path,matrix_path,genecode_path)