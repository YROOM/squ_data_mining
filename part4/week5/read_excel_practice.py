import pandas as pd
import matplotlib.pyplot as plt


studf = pd.read_excel('D:\squ_course_info\数据挖掘\【书圈】684008Python数据挖掘技术及应用PPT数据集源代码\【书圈】684008Python数据挖掘技术及应用PPT数据集源代码\Python数据挖掘技术及应用（第2版）--源代码及数据集--2025-8-20\数据集\chengji.xlsx',
                      sheet_name=1,
                      index_col='Student ID')
print(studf)
ax = studf.plot(kind='line',
          figsize=(5, 5),
           title='scores',

           style=['-','--','-.'],
          )
ax.set_ylabel('fenshu')
plt.show()
