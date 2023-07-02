import pandas as pd 
import os 
import random as rd 


def account_gen_krungsri(data):
    range_account = range(10000,99999)
    range_index = range(0,9)
    
    elemet_account = []
    elemet_account_index = []
    account_list_gen = []

    df_gen_kru = df.loc[df['Bank'] == 'krungsri']

    for i in range_account:
        elemet_account.append(i)

    for i in range_index:
        elemet_account_index.append(i)

 
    i_count = 0

    while i_count < len(df_gen_kru):
        account_gen = ""
        account_e = rd.choice(elemet_account)
        account_in = rd.choice(elemet_account_index)
        account_gen =  'XXX-{}-{}-X'.format(account_in, account_e)
        account_list_gen.append(account_gen)
        i_count = i_count + 1
    
    return account_list_gen


def account_gen_kbank(data):
    randChoise = [0,1]
    range_account = range(1000,9999)
 
    
    elemet_account = []
    account_list_gen = []

    df_gen_kbank = df.loc[df['Bank'] == 'Kbank']

    for i in range_account:
        elemet_account.append(i)

    i_count = 0

    while i_count < len(df_gen_kbank):

        rand_choise = rd.choice(randChoise)
        account_gen = ""

        if rand_choise == 0:
            account_e = rd.choice(elemet_account)
            account_gen =  'XXX-X-X{}-X'.format(account_e)
            account_list_gen.append(account_gen)
            i_count = i_count + 1

        if rand_choise == 1:
            account_e = rd.choice(elemet_account)
            account_gen =  '%%%-%-%{}-%'.format(account_e)
            account_list_gen.append(account_gen)
            i_count = i_count + 1

    return account_list_gen


def concat_gen_account(data, acc_kbank, acc_krungsri):
    df_gen_kru = df.loc[df['Bank'] == 'krungsri']
    df_gen_kbank = df.loc[df['Bank'] == 'Kbank']
    df_gen_kru['gen_acc'] = acc_krungsri
    df_gen_kbank['gen_acc'] = acc_kbank
    df_acc_gen = pd.concat([df_gen_kru, df_gen_kbank])
    return df_acc_gen


df = pd.read_csv('./bb_27092021.csv')
krungsri_accountgen = account_gen_krungsri(data=df)
kbank_accountgen = account_gen_kbank(data=df)
data = concat_gen_account(data=df, acc_kbank= kbank_accountgen, acc_krungsri= krungsri_accountgen)
data.to_csv('bb_19102021.csv')
 

 