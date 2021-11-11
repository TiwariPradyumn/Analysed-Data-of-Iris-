import statistics as st
import numpy as np
import pandas as pd
#reading json file
json_data=pd.read_json("C:\\Users\\p8928\\Documents\\iris.json")
#converting json file into csv file
csv_data=json_data.to_csv()
iris_csv_data=pd.read_csv("C:\\Users\\p8928\\Documents\\iris_csv_data.csv")

#finding mean()
print("setosa")
df1=pd.DataFrame({
"sepalLength":[iris_csv_data[iris_csv_data['species']=='setosa'].sepalLength.mean(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalLength.median(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalLength.mode(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalLength.std(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalLength.var()],
"sepalWidth": [iris_csv_data[iris_csv_data['species']=='setosa'].sepalWidth.mean(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalWidth.median(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalWidth.mode(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalWidth.std(),
               iris_csv_data[iris_csv_data['species']=='setosa'].sepalWidth.var()],
"petalLength":[iris_csv_data[iris_csv_data['species']=='setosa'].petalLength.mean(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalLength.median(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalLength.mode(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalLength.std(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalLength.var()] ,
"petalWidth": [iris_csv_data[iris_csv_data['species']=='setosa'].petalWidth.mean(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalWidth.median(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalWidth.mode(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalWidth.std(),
               iris_csv_data[iris_csv_data['species']=='setosa'].petalWidth.var()]             },
               index=['mean','median','mode','std','var']) 
print(df1)

