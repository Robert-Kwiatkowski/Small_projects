class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):

        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = node(value)
                current_node.left_child.parent = current_node

            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = node(value)
                current_node.right_child.parent = current_node

            else:
                self._insert(value, current_node.right_child)

    def generateTree(self, elements_number, max_value):

        from random import randint

        for i in range(0, elements_number):
            element_random = randint(0, max_value)
            self.insert(element_random)

    def printTree(self, deep=0):
        if self.root != None:
            self._printTree(self.root, deep)

    def _printTree(self, current_node, deep):
        if current_node != None:
            self._printTree(current_node.left_child, deep + 1)
            for x in range(0, deep):
                print('....', end='')
            print(str(current_node.value))
            self._printTree(current_node.right_child, deep + 1)


#### MAIN #####
from random import randint

number_of_elements_in_tree = randint(10, 30)
maximal_value_in_tree = randint(0, number_of_elements_in_tree * 2)
tree = binary_tree()
tree.generateTree(number_of_elements_in_tree, maximal_value_in_tree)
tree.printTree()
value_to_insert = randint(0, number_of_elements_in_tree * 2)
print('###########')
print(value_to_insert)
print('##########')
tree.insert(value_to_insert)
tree.printTree()