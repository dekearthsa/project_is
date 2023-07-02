import pandas as pd 
import random as rd 
import numpy as np

def account_gen_krungsri():
    range_account = range(10000,99999)
    range_index = range(0,9)
    elemet_account = []
    elemet_account_index = []
    account_list_gen = []
    for i in range_account:
        elemet_account.append(i)

    for i in range_index:
        elemet_account_index.append(i)

    i_count = 0

    while i_count < 500:
        account_gen = ""
        account_e = rd.choice(elemet_account)
        account_in = rd.choice(elemet_account_index)
        account_gen =  'XXX-{}-{}-X'.format(account_in, account_e)
        account_list_gen.append([account_gen,"krungsri","Account"])
        i_count = i_count + 1
    
    return account_list_gen

    
def account_gen_kbank():
    range_account = range(1000,9999)

    elemet_account = []
    account_list_gen = []


    for i in range_account:
        elemet_account.append(i)

    i_count = 0

    while i_count <  500:

        account_gen = ""

        if i_count < 250:
            account_e = rd.choice(elemet_account)
            account_gen =  'XXX-X-X{}-X'.format(account_e)
            account_list_gen.append([account_gen,"kbank","Account"])
            i_count = i_count + 1

        if i_count >= 250:
            account_e = rd.choice(elemet_account)
            account_gen =  '%%%-%-%{}-%'.format(account_e)
            account_list_gen.append([account_gen,"kbank","Account"])
            i_count = i_count + 1

    return account_list_gen


def account_gen_bll():
    rand_digit = ["0","1","2","3","4","5","6","7","8","9"]
    loop = 0
    set_gen_account = []

    while loop < 500:
        set_inter = 0
        first_digit =""
        sec_digit = ""
        thr_digit = ""

        while set_inter < 3:
            set_char = rd.choice(rand_digit) 
            first_digit += set_char
            set_inter += 1 
        
        set_inter = 0
        set_char = rd.choice(rand_digit)
        sec_digit += set_char

        while set_inter < 3:
            set_char = rd.choice(rand_digit) 
            thr_digit += set_char
            set_inter += 1

        set_inter = 0
        loop += 1

        if loop < 250:
            set_account = '{}-{}-xxx{}'.format(first_digit, sec_digit, thr_digit)
            set_gen_account.append([set_account,"bll","Account"])
        else:
            set_account = '{}-{}-%%%{}'.format(first_digit, sec_digit, thr_digit)
            set_gen_account.append([set_account,"bll","Account"])

    return set_gen_account



def account_gen_scb():
    rand_digit = ["0","1","2","3","4","5","6","7","8","9"]
    loop = 0
    set_gen_account = []

    while loop < 500:
        set_inter = 0
        frist_digit = ""
        sec_digit = ""

        while set_inter < 3:
            set_digit = rd.choice(rand_digit)
            frist_digit += set_digit
            set_inter += 1

        set_digit = rd.choice(rand_digit)
        sec_digit += set_digit
        set_inter = 0

        if loop < 250:
            set_account = 'xxx-xxx{}-{}'.format(frist_digit, sec_digit)
            set_gen_account.append([set_account,"scb","Account"])
        else:
            set_account = '%%%-%%%{}-{}'.format(frist_digit, sec_digit)
            set_gen_account.append([set_account,"scb","Account"])

        loop += 1 
        
    return set_gen_account

acc_scb = account_gen_scb()
acc_krung = account_gen_krungsri()
acc_kbank = account_gen_kbank()
acc_bll = account_gen_bll()
concat_acc = np.array(acc_scb + acc_krung + acc_kbank + acc_bll) 
df = pd.DataFrame(concat_acc, columns=["word","Bank","label"])
df.to_csv('gen_account.csv', encoding='utf-8')
