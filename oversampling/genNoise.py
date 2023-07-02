import pandas as pd 
import numpy as np
import random as rd 


df = pd.read_csv("./perparoverSampleNotUse.csv")
df = df.drop(columns=['Unnamed: 0'])
set_loop = 10


set_name_scb = ["0.00 THB","ธนาคารไทยพาณิชย์","ธนาคารทหารไทยธนชาต","ธนาคารกรุงไทย","ธนาคารกสิกรไทย","พร้อมเพย์","ธนาคารกรุงศรี","ธนาคารกรุงเทพ","โอนยอดที่เหลือ 2400 บาท รวมทั้งหมด 4800","บันทึกช่วยจำ","ข้อมูลเพิ่มเติมจากผู้ให้บริการ","ผู้รับเงินสามารถสแกนคิวอาร์", "โค้ดนี้เพื่อตรวจสอบสถานะ","จำนวนเงิน","จ่ายบิลสำเร็จ", "SCB", "จาก", "ไปยัง", "Biller ID : ", "ID", "รหัสร้านค้า : ", "รหัสธุรกรรม : ", "Biller ID", "รหัสร้านค้า", "รหัสธุรกรรม", ":"]
set_name_bkk = ["0.00 THB","ธนาคารไทยพาณิชย์","ธนาคารทหารไทยธนชาต","ธนาคารกรุงไทย","ธนาคารกสิกรไทย","พร้อมเพย์","ธนาคารกรุงศรี","ธนาคารกรุงเทพ","สแกนเพื่อตรวจสอบ","เลขที่อ้างอิง","หมายเลขอ้างอิง","SCB","หมายเลขอ้างอิง (ถ้ามี)","รหัสอ้างอิงร้านค้า (ถ้ามี)","รหัสร้านค้า","Biller ID","Biller ID:","ไปที่","จาก","HAPPY", "SONGKRAN", "FESTIVAL", "จำนวนเงิน", "รายการสำเร็จ", "ค่าธรรมเนียม 0.00 THB", "ค่าธรรมเนียม"]

arrayThaLang = ['๑','๒','๓','ภ','๔','ถ','ู','ุ','ึ','๕','ค','๖','ต','๗','จ','๘','ข','๙','ช','ๆ','๐','ไ','ำ','ฎ','พ','ฑ','ะ','ธ','ั','ํ','ี','๊','ณ','ร','ฯ','น','ญ','ย','ฐ','บ','ล','ฟ','ฤ','ห','ฆ','ฏ','ก','ด','โ','เ','ฌ','็','้','่','๋','า','ษ','ส','ศ','ว','ซ','ง','ผ','ป','ฉ','แ','อ','ฮ','ิ','ื','์','ท','ม','ฒ','ใ','ฬ','ฦ','ฝ']
arrayEngLang = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
arrayNumLang = ['1','2','3','4','5','6','7','8','9','0']
arraySymLang = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']',';',':','<','>',',','.','?','/','฿','',' ']

set_rd_word = arrayThaLang + arrayEngLang + arrayNumLang + arraySymLang

array_noise = []


for i in range(set_loop):
    for j in range(len(set_name_scb)):
        warp = {
            "word": set_name_scb[j],
            "Bank": "scb",
            "label": "NotUse"
        }
        array_noise.append(warp)
    for j in range(len(set_name_bkk)):
        warp = {
            "word": set_name_bkk[j],
            "Bank": "bll",
            "label": "NotUse"
        }
        array_noise.append(warp)
    for j in range(1500):
        if(j == 499):
            dfrd = df.sample(n=1)
            dfrd = dfrd[['word']].to_dict()
            set_word = list(dfrd['word'].values())[0]
            warp = {
                "word": set_word,
                "Bank": "scb",
                "label": "NotUse"
            }
            array_noise.append(warp)
        elif(j < 500):
            dfrd = df.sample(n=1)
            dfrd = dfrd[['word']].to_dict()
            set_word = list(dfrd['word'].values())[0]
            warp = {
                "word": set_word,
                "Bank": "bll",
                "label": "NotUse"
            }
            array_noise.append(warp)
        else:
            dfrd = df.sample(n=1)
            dfrd = dfrd[['word']].to_dict()
            set_word = list(dfrd['word'].values())[0]
            warp = {
                "word": set_word + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word) + rd.choice(set_rd_word),
                "Bank": "bll",
                "label": "NotUse"
            }
            array_noise.append(warp)

# print(array_noise)

df_noise = pd.DataFrame.from_dict(array_noise)
df_noise.to_csv('gen_noise.csv', encoding='utf-8')