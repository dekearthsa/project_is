import pandas as pd
import numpy as np


df_default = pd.read_csv("./example_data/BB_28112021.csv")
df_default = df_default[['word','Bank','label']]
df_acc = pd.read_csv("./gen_account.csv")
df_amount = pd.read_csv("./gen_amount.csv")
df_name = pd.read_csv("./gen_name.csv")
df_refcode = pd.read_csv("./gen_refcode.csv")
df_timing = pd.read_csv("./gen_timing.csv")
df_noise = pd.read_csv("./gen_noise.csv")

frames = [df_default, df_acc, df_amount, df_name, df_refcode, df_timing, df_noise]
df = pd.concat(frames)
print(df)
# df.to_csv('data_13JUN2023.csv', encoding='utf-8')