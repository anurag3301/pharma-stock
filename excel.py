import pandas as pd
import os
import string
import random
os.chdir("/home/anurag/repo/pharma-stock")
data = pd.read_excel('data.xlsx', sheet_name='Sheet1')

def rand_str(N):
    return ''.join(random.choices(string.ascii_uppercase, k = N))

for i in range(10):
    data = data.append({'med_name':rand_str(12), 'company':rand_str(12),\
            'expiry_date':pd.to_datetime('2021-12-12'), 'inhand_stock':random.randint(1, 1000),\
            'store_stock':random.randint(1, 1000), 'piece':random.randint(1, 1000),\
            'phyl':random.randint(1, 1000)}, ignore_index=True)

data.to_excel('data.xlsx', index=False)
