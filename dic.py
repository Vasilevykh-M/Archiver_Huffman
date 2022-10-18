from huffman import *
def create_dic(file_name):
    with open(file_name,  encoding="utf-16") as file:
        list_node=[]
        i=0
        for line in file:
            str = line.split()
            if i == 0:
                list_node.append(node(symbol = '\n', weight = float(str[0].replace(',', '.'))))
            elif i == 1:
                list_node.append(node(symbol=' ', weight=float(str[0].replace(',', '.'))))
            else:
                list_node.append(node(symbol=str[0], weight=float(str[1].replace(',', '.'))))
            i+=1
        list_node.append(node(weight=0)) #конец файла
        return list_node