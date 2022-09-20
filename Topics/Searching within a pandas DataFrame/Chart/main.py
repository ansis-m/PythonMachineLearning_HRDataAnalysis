# your code here. the dataset is already loaded as food_calories_df.

array = ['CARROTS,RAW',
'BREAD,WHEAT',
'CRANBERRIES,RAW',
'SUGARS,MAPLE',
'WATER,TAP,WELL']

print(sum(food_calories_df[food_calories_df.Shrt_Desc.isin(array)].Energ_Kcal.values.tolist()))
