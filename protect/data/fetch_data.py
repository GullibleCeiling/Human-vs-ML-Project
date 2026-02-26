
import pandas as pd 
import seaborn as sns
import matplotlib as plt
import os
import sys


def get_penguins_data():
    file_path = '/workspaces/Human-vs-ML-Project/protect/data/penguins_size.csv'

    df = pd.read_csv(file_path)
    
    target_name = "species" 
   
    x= df["culmen_depth_mm"]
    
    y= df[target_name]
   
    return df, target_name

#J:

#L 
print(get_penguins_data())