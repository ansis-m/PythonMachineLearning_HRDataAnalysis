import pandas as pd

goods = {
    "type": ['PC', 'monitor', 'printer', 'notebook', 'PC'], 
    "price": [450, 150, 175, 600, 500],
    "quantity": [5, 2, 10, 15, 5],
    "vendor_code": ['135', '960', '004', '420', '114'], 
}
df = pd.DataFrame(goods)

# your code here
print(df.sort_values(['quantity', 'vendor_code'], ascending=False))
