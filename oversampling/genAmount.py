import pandas as pd 
import random as rd 
import numpy as np

def gen_amount_SCB():
    rand_digit = [0,1,2,3,4,5,6,7,8,9]
    rand_digit_without_zero = [1,2,3,4,5,6,7,8,9]
    loop  = 0 
    set_gen_amount = []
    while loop < 600:
        if loop < 100:
            is_amount = rd.choice(rand_digit_without_zero)
            set_amount_scb = str(is_amount)+".00"
            set_gen_amount.append([set_amount_scb,"scb","Amount"])
        elif loop >= 100 and loop < 250:
            sec_loop = 0
            while sec_loop < 2:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                set_amount_scb = str(is_first_amount)+str(is_sec_amount)+".00"
                set_gen_amount.append([set_amount_scb,"scb","Amount"])
                sec_loop += 1
        elif loop >= 250 and loop < 400:
            sec_loop = 0
            while sec_loop < 3:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                set_amount_scb = str(is_first_amount)+str(is_sec_amount)+str(is_thr_amount)+".00"  
                set_gen_amount.append([set_amount_scb,"scb","Amount"])
                sec_loop += 1
        elif loop >= 400 and loop < 500:
            sec_loop = 0
            while sec_loop < 4:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                is_four_amount = rd.choice(rand_digit)
                set_amount_scb = str(is_first_amount)+","+str(is_sec_amount)+str(is_thr_amount)+str(is_four_amount)+".00"  
                set_gen_amount.append([set_amount_scb,"scb","Amount"])
                sec_loop += 1
        elif loop >= 500 and loop < 600:
            sec_loop = 0
            while sec_loop < 4:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                is_four_amount = rd.choice(rand_digit)
                is_fit_amount = rd.choice(rand_digit)
                set_amount_scb = str(is_first_amount)+str(is_fit_amount)+","+str(is_sec_amount)+str(is_thr_amount)+str(is_four_amount)+".00"  
                set_gen_amount.append([set_amount_scb,"scb","Amount"])
                sec_loop += 1
        loop += 1
    
    
    return set_gen_amount



def gen_amount_krung():
    rand_digit = [0,1,2,3,4,5,6,7,8,9]
    rand_digit_without_zero = [1,2,3,4,5,6,7,8,9]
    loop  = 0 
    set_gen_amount = []
    while loop < 600:
        if loop < 100:
            is_amount = rd.choice(rand_digit_without_zero)
            set_amount_krungsri = str(is_amount)+".00 THB"
            set_gen_amount.append([set_amount_krungsri,"krungsri","Amount"])
        elif loop >= 100 and loop < 250:
            sec_loop = 0
            while sec_loop < 2:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                set_amount_krungsri = str(is_first_amount)+str(is_sec_amount)+".00 THB"
                set_gen_amount.append([set_amount_krungsri,"krungsri","Amount"])
                sec_loop += 1
        elif loop >= 250 and loop < 400:
            sec_loop = 0
            while sec_loop < 3:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                set_amount_krungsri = str(is_first_amount)+str(is_sec_amount)+str(is_thr_amount)+".00 THB"
                set_gen_amount.append([set_amount_krungsri,"krungsri","Amount"])
                sec_loop += 1
        elif loop >= 400 and loop < 500:
            sec_loop = 0
            while sec_loop < 4:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                is_four_amount = rd.choice(rand_digit)
                set_amount_krungsri = str(is_first_amount)+str(is_sec_amount)+str(is_thr_amount)+str(is_four_amount)+".00 THB"
                set_gen_amount.append([set_amount_krungsri,"krungsri","Amount"])
                sec_loop += 1
        elif loop >= 500 and loop < 600:
            sec_loop = 0
            while sec_loop < 4:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                is_four_amount = rd.choice(rand_digit)
                is_fit_amount = rd.choice(rand_digit)
                set_amount_scb = str(is_first_amount)+str(is_fit_amount)+","+str(is_sec_amount)+str(is_thr_amount)+str(is_four_amount)+".00 THB"  
                set_gen_amount.append([set_amount_scb,"krungsri","Amount"])
                sec_loop += 1
        loop += 1
    return set_gen_amount

def gen_amount_kbank():
    rand_digit = [0,1,2,3,4,5,6,7,8,9]
    rand_digit_without_zero = [1,2,3,4,5,6,7,8,9]
    loop  = 0 
    set_gen_amount = []
    while loop < 600:
        if loop < 100:
            is_amount = rd.choice(rand_digit_without_zero)
            set_amount_kbank = str(is_amount)+".00 บาท"
            set_gen_amount.append([set_amount_kbank,"kbank","Amount"])
        elif loop >= 100 and loop < 250:
            sec_loop = 0
            while sec_loop < 2:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                set_amount_kbank = str(is_first_amount)+str(is_sec_amount)+".00 บาท"
                set_gen_amount.append([set_amount_kbank,"kbank","Amount"])
                sec_loop += 1
        elif loop >= 250 and loop < 400:
            sec_loop = 0
            while sec_loop < 3:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                set_amount_kbank = str(is_first_amount)+str(is_sec_amount)+str(is_thr_amount)+".00 บาท"
                set_gen_amount.append([set_amount_kbank,"kbank","Amount"])
                sec_loop += 1
        elif loop >= 400 and loop < 500:
            sec_loop = 0
            while sec_loop < 4:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                is_four_amount = rd.choice(rand_digit)
                set_amount_kbank = str(is_first_amount)+str(is_sec_amount)+str(is_thr_amount)+str(is_four_amount)+".00 บาท"
                set_gen_amount.append([set_amount_kbank,"kbank","Amount"])
                sec_loop += 1
        elif loop >= 500 and loop < 600:
            sec_loop = 0
            while sec_loop < 4:
                is_first_amount = rd.choice(rand_digit_without_zero)
                is_sec_amount = rd.choice(rand_digit)
                is_thr_amount = rd.choice(rand_digit)
                is_four_amount = rd.choice(rand_digit)
                is_fit_amount = rd.choice(rand_digit)
                set_amount_scb = str(is_first_amount)+str(is_fit_amount)+","+str(is_sec_amount)+str(is_thr_amount)+str(is_four_amount)+".00 บาท"  
                set_gen_amount.append([set_amount_scb,"kbank","Amount"])
                sec_loop += 1
        loop += 1
    return set_gen_amount

amount_scb = gen_amount_SCB()
amount_krung = gen_amount_krung()
amount_kbank = gen_amount_kbank() ## same as bll format
concat_amount = np.array(amount_scb + amount_krung + amount_kbank)
df = pd.DataFrame(concat_amount, columns=["word","Bank","label"])
df.to_csv('gen_amount.csv', encoding='utf-8')


