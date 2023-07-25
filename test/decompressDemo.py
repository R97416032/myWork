
from utils.decompress import *

path= "../data/compress/GSE113660/GSE113660_RAW.tar"
un_tar(path)
paths=os.listdir(path.replace(".tar",""))
for p in paths:
    un_gz(path.replace(".tar","/")+p)