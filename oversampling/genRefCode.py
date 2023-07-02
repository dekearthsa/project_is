import pandas as pd 
import random as rd 
import numpy as np 


def refCode_SCB():
    array_ref_code = []
    set_year = ["2020","2021","2023","2024","2025"]
    set_month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    set_day = ["01","02","03","04","05","06","07","08","09","10",
               "11","12","13","14","15","16","17","18","19","20",
               "21","22","23","24","25","26","27","28","29","30","31"]
    set_digit = [1,2,3,4,5,6,7,8,9,0]
    arrayEngLang = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',"1","2","3","4","5","6","7","8","9","0"]
    loop = 0
    while loop < 1000:
        loop_create_string = 0
        rd_year = rd.choice(set_year)
        rd_month = rd.choice(set_month)
        rd_day = rd.choice(set_day)
        rd_num = rd.choice(set_digit)
        set_first_string = rd_year+rd_month+rd_day+str(rd_num)
        ref_back_string = ""
        while loop_create_string < 17:
            set_string_ref = rd.choice(arrayEngLang)
            ref_back_string = ref_back_string+set_string_ref
            loop_create_string += 1
        set_first_string = set_first_string+ref_back_string
        array_ref_code.append([set_first_string, "scb", "RefCode"])
        loop += 1
    return array_ref_code

def refCode_krung():
    set_digit = ["0","1","2","3","4","5","6","7","8","9"]
    constant_refcode = "BAYM"
    loop = 0
    array_ref_code = []
    while loop < 1000:
        set_range = 0
        concat_digit = constant_refcode
        while set_range < 9:
            rd_digit = rd.choice(set_digit)
            concat_digit = concat_digit+rd_digit
            set_range += 1
        array_ref_code.append([concat_digit,"krungsri", "RefCode"])
        loop += 1 
    return array_ref_code

def refCode_kbank():
    array_ref_code = []
    set_digit = ["0","1","2","3","4","5","6","7","8","9"]
    loop = 0
    while loop < 1000:
        loop_create_string = 0
        refcode = ""
        while loop_create_string < 18:
            rd_num = rd.choice(set_digit)
            refcode = refcode+rd_num
            loop_create_string += 1
        array_ref_code.append([refcode, "kbank", "RefCode"])
        loop += 1
    return array_ref_code

def refCode_bll():
    array_ref_code = []
    set_year = ["2020","2021","2023","2024","2025"]
    set_month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    set_day = ["01","02","03","04","05","06","07","08","09","10",
               "11","12","13","14","15","16","17","18","19","20",
               "21","22","23","24","25","26","27","28","29","30","31"]
    set_digit = [1,2,3,4,5,6,7,8,9,0]
    loop = 0
    while loop < 1000:
        rd_year = rd.choice(set_year)
        rd_month = rd.choice(set_month)
        rd_day = rd.choice(set_day)
        loop_create_string = 0
        string_date = rd_year+rd_month+rd_day
        string_num = ""
        while loop_create_string < 17:
            rd_num = rd.choice(set_digit)
            string_num = string_num+str(rd_num)
            loop_create_string += 1
        string_date = string_date+string_num
        array_ref_code.append([string_date, "bll", "RefCode"])
        loop += 1
    return array_ref_code


ref_scb = refCode_SCB()
ref_krung = refCode_krung()
ref_kbank = refCode_kbank()
ref_bll = refCode_bll()
concat_amount = np.array(ref_scb + ref_krung + ref_kbank + ref_bll)
print(concat_amount)
df = pd.DataFrame(concat_amount, columns=["word", "Bank", "label"])
df.to_csv('gen_refcode.csv', encoding='utf-8')