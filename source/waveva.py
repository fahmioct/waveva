import numpy as np
import pandas as pd
# from pathlib import Path
import glob

# df = pd.read_csv(Path("/home/hoream/Documents/waveva/sample/*.txt")
# df = pd.read_csv("\*.txt")

path = r'/home/hoream/Documents/waveva/sample/'
all_files = glob.glob(path+'*.txt')

li = []
for filename in all_files:
    df=pd.read_csv(filename, delimiter="/t")
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print(frame)