
from tool_function import Ner
from tool_function import sentence_boundary_detection


def main():
    model = Ner("/home/ypd-19-2/BERT/BERT-BER-dev/output/output12")
    input = sentence_boundary_detection('/home/ypd-19-2/SpERT/data/101016jjpowsour201110077.txt')
    output = []
    string_list = []
    for sent in input:
        output_temp = model.predict(sent)
        output.append(output_temp)
    for temp_list in output:
        temp1 = []
        for temp_dict in temp_list:
            temp1.append(temp_dict['word'])
            temp1.append("("+temp_dict['tag']+")")
        str_temp1 = " ".join(temp1)
        string_list.append(str_temp1)
    out_string = "\n".join(string_list)
    print('bupt')




    print('bupt')

if __name__ == '__main__':
    main()