import pandas as pd 
import numpy as np
import random as rd 
import string

def setFuncFristWord ():
    list_name = pd.read_csv("./list_name/List_name.csv")
    set_array_eng = []
    set_array_name = []
    set_bank = ["kbank","bll","scb","krungsri"]
    for i in string.ascii_lowercase:
        set_array_eng.append(i)

    for i in string.ascii_uppercase:
        set_array_eng.append(i)

    for idx, row in list_name.iterrows():
        set_al = row['name'][0]
        rd_bank = rd.choice(set_bank)
        if set_al in set_array_eng:
            gen_word = row['name'].replace(u'\xa0', u' ')
            set_array_name.append([gen_word,rd_bank,"Name"])
        else:
            if idx < 250:
                gen_word = 'นาย ' +  row['name']
                gen_word = gen_word.replace(u'\xa0', u' ')
                set_array_name.append([gen_word,rd_bank,"Name"])
            elif 250 <= idx < 500:
                gen_word = 'น.ส. ' +  row['name']
                gen_word = gen_word.replace(u'\xa0', u' ')
                set_array_name.append([gen_word,rd_bank,"Name"])
            elif 750 <= idx < 1050:
                gen_word = 'นาง ' +  row['name']
                gen_word = gen_word.replace(u'\xa0', u' ')
                set_array_name.append([gen_word,rd_bank,"Name"])

    return set_array_name


gen_name = setFuncFristWord()
df = pd.DataFrame(gen_name, columns=["word","Bank","label"])
df.to_csv('gen_name.csv', encoding='utf-8')