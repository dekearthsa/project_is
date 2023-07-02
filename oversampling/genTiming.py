import pandas as pd 
import numpy as np 
import random as rd 

def gen_timing(bank):
    set_num = ["1","2","3","4","5","6","7","8","9","0"]
    set_loop_hours = 0
    set_loop_min = 0
    set_loop_sec = 0

    gen_hours = ""
    gen_min = ""
    gen_sec = ""

    if bank != "krungsri":
        while set_loop_hours < 2:
            rd_f = rd.choice(set_num)
            rd_sec = rd.choice(set_num)
            convert_int = int(rd_f+rd_sec)
            if convert_int < 24:
                if convert_int < 10:
                    gen_hours = "0"+str(convert_int)
                    set_loop_hours += 1
                else: 
                    gen_hours = str(convert_int)
                    set_loop_hours += 1

        while set_loop_min < 2:
            rd_f = rd.choice(set_num)
            rd_sec = rd.choice(set_num)
            convert_int = int(rd_f+rd_sec)
            if convert_int < 60:
                if convert_int < 10:
                    gen_min = "0"+str(convert_int)
                    set_loop_min += 1
                else: 
                    gen_min = str(convert_int)
                    set_loop_min += 1

        if bank == "kbank":
            set_timing = gen_hours+":"+gen_min+" "+"น."
            return set_timing
        else: 
            set_timing = gen_hours+":"+gen_min
            return set_timing

    if bank == "krungsri":
        while set_loop_hours < 2:
            rd_f = rd.choice(set_num)
            rd_sec = rd.choice(set_num)
            convert_int = int(rd_f+rd_sec)
            if convert_int < 24:
                if convert_int < 10:
                    gen_hours = "0"+str(convert_int)
                    set_loop_hours += 1
                else: 
                    gen_hours = str(convert_int)
                    set_loop_hours += 1
        
        while set_loop_min < 2:
            rd_f = rd.choice(set_num)
            rd_sec = rd.choice(set_num)
            convert_int = int(rd_f+rd_sec)
            if convert_int < 60:
                if convert_int < 10:
                    gen_min = "0"+str(convert_int)
                    set_loop_min += 1
                else: 
                    gen_min = str(convert_int)
                    set_loop_min += 1

        while set_loop_sec < 2:
            rd_f = rd.choice(set_num)
            rd_sec = rd.choice(set_num)
            convert_int = int(rd_f+rd_sec)
            if convert_int < 60:
                if convert_int < 10:
                    gen_sec = "0"+str(convert_int)
                    set_loop_sec += 1
                else: 
                    gen_sec = str(convert_int)
                    set_loop_sec += 1
        set_timing = gen_hours+":"+gen_min+":"+gen_sec
        return set_timing


def gen_time_scb():
    set_year = ["2562","2563","2564","2565","2566"]
    set_month = ["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]
    set_day = ["01","02","03","04","05","06","07","08","09","10",
               "11","12","13","14","15","16","17","18","19","20",
               "21","22","23","24","25","26","27","28","29","30","31"]
    array_time = []
    loop = 0
    while loop < 1000:
        rd_day = rd.choice(set_day)
        rd_month = rd.choice(set_month)
        rd_year = rd.choice(set_year)
        set_timing = gen_timing("scb")
        gen_word = rd_day+" "+rd_month+" "+rd_year+" "+set_timing
        array_time.append([gen_word,"scb","Timing"])
        loop+= 1
    return array_time

def gen_time_krung():
    set_year = ["2562","2563","2564","2565","2566"]
    set_month = ["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]
    set_day = ["01","02","03","04","05","06","07","08","09","10",
               "11","12","13","14","15","16","17","18","19","20",
               "21","22","23","24","25","26","27","28","29","30","31"]
    array_time = []
    loop = 0
    while loop < 1000:
        rd_day = rd.choice(set_day)
        rd_month = rd.choice(set_month)
        rd_year = rd.choice(set_year)
        set_timing = gen_timing("krungsri")
        gen_word = rd_day+" "+rd_month+" "+rd_year+" "+set_timing
        array_time.append([gen_word,"krungsri","Timing"])
        loop+= 1
    return array_time

def gen_time_kbank():
    set_year = ["62","63","64","65","66"]
    set_month = ["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]
    set_day = ["01","02","03","04","05","06","07","08","09","10",
               "11","12","13","14","15","16","17","18","19","20",
               "21","22","23","24","25","26","27","28","29","30","31"]
    array_time = []
    loop = 0
    while loop < 1000:
        rd_day = rd.choice(set_day)
        rd_month = rd.choice(set_month)
        rd_year = rd.choice(set_year)
        set_timing = gen_timing("kbank")
        gen_word = rd_day+" "+rd_month+" "+rd_year+" "+set_timing
        array_time.append([gen_word,"kbank","Timing"])
        loop+= 1
    return array_time

def gen_time_bll():
    set_year = ["62","63","64","65","66"]
    set_month = ["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]
    set_day = ["01","02","03","04","05","06","07","08","09","10",
               "11","12","13","14","15","16","17","18","19","20",
               "21","22","23","24","25","26","27","28","29","30","31"]
    array_time = []
    loop = 0
    while loop < 1000:
        rd_day = rd.choice(set_day)
        rd_month = rd.choice(set_month)
        rd_year = rd.choice(set_year)
        set_timing = gen_timing("bll")
        gen_word = rd_day+" "+rd_month+" "+rd_year+", "+set_timing
        array_time.append([gen_word,"bll","Timing"])
        loop+= 1
        
    return array_time


array_gen_time_scb = gen_time_scb()
array_gen_time_krung = gen_time_krung()
array_gen_time_kbank = gen_time_kbank()
array_gen_time_bll = gen_time_bll()
concat_array = array_gen_time_scb+array_gen_time_krung+array_gen_time_kbank+array_gen_time_bll
df = pd.DataFrame(concat_array, columns=["word", "Bank", "label"])
df.to_csv('gen_timing.csv', encoding='utf-8')