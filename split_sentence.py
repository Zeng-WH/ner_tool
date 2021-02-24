import tqdm
import spacy

def sentence_boundary_detection(input_dir):
    sentence_list = []
    nlp = spacy.load('en')
    with open(input_dir, 'r') as f: #打开文件
        data = f.readlines() #读取文件
        for line in data:
            doc = nlp(line)
            for sent in doc.sents:
                if len(sent) < 2:
                    continue
                else:
                    sentence_list.append(sent.text)
                #print(len(sent.text))
    return sentence_list

a =sentence_boundary_detection('/home/ypd-19-2/SpERT/data/101016jmatchemphys200710005.txt')
print('test')
