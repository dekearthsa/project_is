import pytesseract 
from PIL import Image
import os
import pandas as pd

path_dir = "./myS3/image_bkk"
ext = ('.jpg', '.png')

BANK = "BLL"
raw_data_file_name = "raw_data_bll"


word = ""
word_left = []
word_top = []
word_width = []
word_height = []
page_num = []
block_num = []
par_num = []
line_num = []
word_num = []
conf = []

dataFrame = []

for iterate, file in enumerate(os.listdir(path_dir)):
    print(file)
    img = Image.open("./myS3/image_bkk/"+file)
    raw_data = pytesseract.image_to_data(img, lang='tha+eng', output_type='data.frame')

    for idx,i in enumerate(raw_data.conf):
        if raw_data['level'][idx] == 5:
            word = word + raw_data['text'][idx]
            word_left.append(raw_data['left'][idx])
            word_top.append(raw_data['top'][idx])
            word_width.append(raw_data['width'][idx])
            word_height.append(raw_data['height'][idx])
            page_num.append(raw_data['page_num'][idx])
            block_num.append(raw_data['block_num'][idx])
            par_num.append(raw_data['par_num'][idx])
            line_num.append(raw_data['line_num'][idx])
            word_num.append(raw_data['word_num'][idx])
            conf.append(raw_data['conf'][idx])
        else:
            if word != "":
                average_word_left = round(sum(word_left) / len(word_left),2)
                average_word_top = round(sum(word_top) / len(word_top), 2)
                average_word_width = round(sum(word_width) / len(word_width),2)
                average_word_height = round(sum(word_height) / len(word_height), 2)
                average_page_num = round(sum(page_num)/ len(page_num), 2)
                average_block_num = round(sum(block_num) / len(block_num), 2)
                average_par_num = round(sum(par_num) / len(par_num), 2)
                average_line_num = round(sum(line_num) / len(line_num), 2)
                average_word_num = round(sum(word_num) / len(word_num), 2)
                average_conf = round(sum(conf) / len(conf), 2)
                warp = {
                    'bank':BANK,
                    'level':5,
                    'page_num': average_page_num,
                    'block_num': average_block_num,
                    'par_num': average_par_num,
                    'line_num': average_line_num,
                    'word_num': average_word_num,
                    'left' : average_word_left,
                    'top': average_word_top,
                    'width': average_word_width,
                    'height': average_word_height,
                    'conf': average_conf,
                    'word': word
                }

                dataFrame.append(warp)
                word = ""
                word_left.clear()
                word_top.clear()
                word_width.clear()
                word_height.clear()
                page_num.clear()
                block_num.clear()
                par_num.clear()
                line_num.clear()
                word_num.clear()
                conf.clear()


featureName = ['bank','level','page_num','block_num','par_num','line_num','word_num','left','top','width','height','conf','word']
df = pd.DataFrame(dataFrame, columns= featureName)
df.to_csv(raw_data_file_name+'.csv')