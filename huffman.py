'''
    File: huffman.py
    Author: John Le
    Purpose: Takes in a preorder and inorder traversal of a decoding tree and
    an encoded sequence and then returns the postorder traversal and a 
    decoded sequence of values.
    CSC 120, 001, Spring Semester
'''

class BinaryTree:
    '''A class for a binaryTree, initializes a node
    where value is the base and right and left nodes
    are None.
    Parameters: value is an integer
    Return Value: prints a representation of a binary tree'''
    def __init__(self, value):
        # initializes a tree node.
        # attribute values are all None except the base
        self._base = value
        self._left = None
        self._right = None
    
    def __str__(self):
        # returns a string representation of the binary tree
        if self._base == None:
            return "None"
        else:
            return ("({:d} {} {})".format( int(self._base), str(self._left), str(self._right)))
            

def processFile(file):
    '''Opens a file and processes it according, removing "\n"
    and appending the lines processed to a list.
    Parameters: file is a string
    Pre-Condition: file is a string
    Post-Condition: returns a list of strings'''
    fileInput = open(file, "r")
    numbers = []

    # processes the file inputted and adds each line
    # to a list
    for line in fileInput:
        line = line.strip("\n")
        numbers.append(line)

    fileInput.close()

    return numbers

def constructBinaryTree(preorder, inorder):
    '''Constructs a binary tree from a given preorder
    and inorder sequence.
    Parameters: preorder is a string, inorder is a string
    Pre-Condition: preorder is a string, inorder is a string
    Post-Condition: returns a binary tree that is in a specific order
    according to the preorder and inorder sequences specified'''
    x = len(preorder)
    if x == 0:
        return None

    if x == 1:
        return BinaryTree(preorder[0])

    root = 0
    for i in range(x):
        if inorder[i] == preorder[0]:
            root = i
            break

    node = BinaryTree(preorder[0])
    inorder1 = inorder[0:root]
    inorder2 = inorder[root + 1:]
    preorder1 = preorder[1:root + 1]
    preorder2 = preorder[root + 1:]
    node._left = constructBinaryTree(preorder1, inorder1)
    node._right = constructBinaryTree(preorder2, inorder2)

    return node
        
def is_leaf(node):
    '''Checks a node to see if it is a leaf or not and
    returns true or false depending on if it is a leaf
    or not
    Paramters: node is a BinaryTree object
    Pre-Condition: node is a BinaryTree object
    Post-Condition: returns true or false'''
    if node == None:
        return False

    elif node._left == None and node._right == None:
        return True

    return False

def postorder(tree):
    '''Prints the postorder of a given binary tree
    Parameters: tree is a BinaryTree object
    Pre-Condition: tree is a BinaryTree object
    Post-Condition: prints the postorder of a
    given binary tree'''
    if tree == None:
        return

    postorder(tree._left)
    postorder(tree._right)

    print(tree._base, end = " ")

def decode_values(tree,decode):
    '''Decodes given binary directions on a binary tree
    and returns the values visited.
    Parameters: tree is a BinaryTree object, decode is a string
    Pre-Condition: tree is a BinaryTree object, decode is a string
    Post-Condition: prints the values visited according
    to the decoded string'''
    if tree == None or is_leaf(tree) == None:
        return

    n = len(decode)
    i = 0
    temp = tree

    while(i < n):
        if decode[i] =='0' :
            temp=temp._left
        else:
            temp=temp._right

        if(temp==None):
            temp = tree

        elif(is_leaf(temp)):
            print(temp._base, end="")
            temp = tree

        i += 1

def main():
    '''Prompts the user for a file to open, then processes
    and calls the functions needed to print the postorder and
    decoded sequence of the binary tree generated from the 
    opened file.
    Parameters: N/A
    Pre-Condition: N/A
    Post-Condition: Prints the postorder and decoded
    sequence of the binary tree generated'''
    fileInput = input("Input file: ")
    preorder = processFile(fileInput)[0]
    inorder = processFile(fileInput)[1]
    decode = processFile(fileInput)[2]
    preorder = preorder.replace(" ", "")
    inorder = inorder.replace(" ", "")

    tree = constructBinaryTree(preorder, inorder)
    postorder(tree)
    print()
    decode_values(tree, decode)
    print()

main()