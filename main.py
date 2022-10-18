from huffman import *
from compression import *
from decompression import *
import dic

FILE_FREQ = r"C:\Users\Михаил\Desktop\Прога\Прога чистая\Комбинаторки\Архиватор\data\freq.txt"
FILE_COMPR = r"C:\Users\Михаил\Desktop\Прога\Прога чистая\Комбинаторки\Архиватор\data\etalon2.txt"
FILE_BIN = r"C:\Users\Михаил\Desktop\Прога\Прога чистая\Комбинаторки\Архиватор\data\rez.bin"
FILE_RES = r"C:\Users\Михаил\Desktop\Прога\Прога чистая\Комбинаторки\Архиватор\data\rez1.txt"

if __name__ == '__main__':
    lst = dic.create_dic(FILE_FREQ)
    tree = huffman_tree(lst)
    tree.create_tree()
    tree.code_huffman(tree.root, '')

    comp = compression(
        FileNameInput = FILE_COMPR,
        FileNameOtput = FILE_BIN,
        dict = tree.dic)
    comp.compres()

    decomp = decompression(
        FileNameInput = FILE_BIN,
        FileNameOtput = FILE_RES,
        root = tree.root)
    decomp.decompres()