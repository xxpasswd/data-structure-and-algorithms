'''
将这样的 "#### 4. factorial:数n的阶乘，后面有几个零" 匹配出来
替换为 "#### [4. factorial:数n的阶乘，后面有几个零](./factorial.py)"
'''

import re
import os

pattern = r'(?<=#### )(\d+[ .]*(\w+).*)'

with open('README.md','r') as f:
    f2 = open('temp','w')
    for i in f:
        res = re.sub(pattern,r'[\1](./\2.py)',i)
        f2.write(res)

f2.close()
os.rename('temp','README.md')
