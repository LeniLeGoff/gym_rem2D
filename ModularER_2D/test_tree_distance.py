#! /usr/bin/python3

from Encodings import Network_Encoding as cppn
from Encodings import LSystem as ls
from Encodings import Direct_Encoding as de
import Tree as tr
from gym_rem2D.morph import SimpleModule, CircularModule2D

def get_module_list():
    module_list = []
    for i in range(4):
        module_list.append(SimpleModule.Standard2D())
    for i in range(4):
        module_list.append(CircularModule2D.Circular2D())
    return module_list

def random_tree():
    '''Create random trees from cppn encoding'''
    moduleList = get_module_list()
    genome = ls.NN_enc(moduleList,"CPPN")
    tree_depth = 8
    return genome.create(tree_depth)

if __name__ == '__main__':
    #create two random trees
    tree1 = random_tree()
    tree1.create_children_lists()
    tree2 = random_tree()
    tree2.create_children_lists()
    print("structure of tree 1")
    tree1.print_structure()
    print("structure of tree 2")
    tree2.print_structure()

    print(tr.Tree.distance(tree1,tree2))

