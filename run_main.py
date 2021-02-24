import sys
import matplotlib
import tkinter
from tkinter import filedialog
from tool_function import Ner
from tool_function import sentence_boundary_detection
from tkinter import StringVar, IntVar
from tkinter import *


def process_ner():
    label_list = []
    file_path = filedialog.askopenfilename()
    input = sentence_boundary_detection(file_path)
    output = []
    for sent in input:
        output_temp = model.predict(sent)
        output.append(output_temp)
    for temp_list in output:
        temp1 = []
        for temp_dict in temp_list:
            temp1.append(temp_dict['word'])
            temp1.append("("+temp_dict['tag']+")")
        str_temp1 = " ".join(temp1)
        temp2 = tkinter.Label(top, text=str_temp1)
        temp2.pack(fill=0)
        label_list.append(temp2)

    print(output)
def ner_result():
    file_path = filedialog.askopenfilename()
    input = sentence_boundary_detection(file_path)
    output = []
    string_list = []
    for sent in input:
        output_temp = model.predict(sent)
        output.append(output_temp)
    for temp_list in output:
        temp1 = []
        for temp_dict in temp_list:
            temp1.append(temp_dict['word'])
            temp1.append("(" + temp_dict['tag'] + ")")
        str_temp1 = " ".join(temp1)
        string_list.append(str_temp1)
    out_string = "\n".join(string_list)
    print(out_string)
    secon = Toplevel()
    secon.title('NER Result')
    scroll = Scrollbar(secon)
    # 创建滚动条
    # 创建文本框text
    text = Text(secon)
    scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
    text.pack(side=tkinter.LEFT,fill=tkinter.X) # 将文本框填充进wuya窗口的左侧，
    # 将滚动条与文本框关联
    scroll.config(command=text.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
    text.config(yscrollcommand=scroll.set)  # 将滚动条关联到文本框
    text.insert('insert', out_string)







def load_model():
    fold_path = filedialog.askdirectory()
    global model
    model = Ner(fold_path)
    print(model)


import tkinter
top = tkinter.Tk(screenName=':10.0')
top.title('Mater-BERT')

top.attributes('-fullscreen', True)


# 创建标签，用于显示内容

menubar = tkinter.Menu(top)
menubar.add_command(label="Model", command=load_model)
menubar.add_command(label="NER", command=ner_result)
top.config(menu=menubar)
# 进入消息循环
top.mainloop()
