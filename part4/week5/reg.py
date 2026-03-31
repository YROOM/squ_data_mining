# import re
#
# # 手机号正则
# pattern = r'^1[3-9]\d{9}$'
#
# phone = input("请输入手机号：")
#
# if re.match(pattern, phone):
#     print("✅ 手机号格式正确")
# else:
#     print("❌ 手机号格式错误")

import re

text = "联系人：张三 13812345678，李四 13998765432"

phones = re.findall(r'1[3-9]\d{9}', text)
print("提取到手机号：", phones)