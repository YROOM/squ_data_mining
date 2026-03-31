import numpy as np
import pandas as pd
data_read = {
    "name":["Jack","Mary","John","Alice"],
    "age":[10,20,30,40],
    "weight":[30,40,55,65]
}
df = pd.DataFrame(data_read)
print(df)

ans_after_drop = df.drop(columns='age',inplace=True)

print("删除之后原来的df:",df)

