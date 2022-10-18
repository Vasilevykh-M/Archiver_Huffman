from textwrap import wrap

#класс листа
class node:
    def __init__(self, symbol='', weight = 0, L = None, R = None):
        self.symbol=symbol # символ
        self.weight=weight # вес узла
        self.L=L # левый потомок
        self.R=R # правый потомок

    def __str__(self):
        return 'Symbol \'{0}\' Weight = {1}'.format(self.symbol, self.weight)

# класс дерева
class huffman_tree:

    def __init__(self, list_nodes):
        self.dic = {}
        self.nodes = list_nodes
        self.root = None


    def convert_to_bytes(self, code): # приведение к байтам
        nums = wrap(code, 8)
        bts = []
        for num in nums:
            bts.append(int(num, 2))
        return bytes(bts)


    def create_tree(self): #создание дерева методом Хаффмана
        while len(self.nodes) > 1:
            self.nodes.sort(key=lambda x: x.weight)
            new_node = node(weight=(self.nodes[0].weight+self.nodes[1].weight),
                            L = self.nodes[0], R = self.nodes[1])
            self.nodes.pop(0)
            self.nodes.pop(0)
            self.nodes.append(new_node)

        self.root = self.nodes[0] #передаем корень

    def code_huffman(self, Node, code): # получение кода Хаффмана для каждого символа (рекуррентно)
        if Node.L == None or Node.R == None:
            while len(code)%8!=0:   # добивания байтов
                code+='0'
            self.dic[Node.symbol]=self.convert_to_bytes(code)
            return
        self.code_huffman(Node.L, code + '0')
        self.code_huffman(Node.R, code + '1')
