# -*- coding: utf-8 -*-
"""
Algorithm in Python

Binary Tree

@author: jychang
"""

from turtle import *
shape('turtle')

def draw_node(x,y,text):
    up()
    goto(x-8,y-15)
    down()
    write(text, font=("Arial", 20, "bold"))
    up()
    goto(x,y-20)
    down()
    seth(0)
    circle(20)
    up()
    goto(x,y)
    down()

def draw_edge(x, y, left):
    up()
    goto(x,y-20)
    seth(0)
    if left:
        circle(20,-45)
        seth(225)
    else:
        circle(20,45)
        seth(-45)
    down()
    fd(30)
    seth(0)
    
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None   

    def search_tree(self, key):
        if self.data == key:
            return self
        if key < self.data:
            if self.left:
                return self.left.search_tree(key)
        else:
            if self.right:
                return self.right.search_tree(key)
        return None

    def insert_tree(self, new_node):
        if self.data > new_node.data:
            if self.left is None:
                self.left = new_node
                new_node.parent = self
            else:
                self.left.insert_tree(new_node)
        else:
            if self.right is None:
                self.right = new_node
                new_node.parent = self
            else:
                self.right.insert_tree(new_node)

    def find_minimum(self):
        min_node = self
        while min_node.left:
            min_node = min_node.left
        return min_node

    def find_maximum(self):
        max_node = self
        while max_node.right:
            max_node = max_node.right
        return max_node

    def tree_traversal(self):
        if self.left:
            self.left.tree_traversal()
        print(self.data, end=' ')
        if self.right:
            self.right.tree_traversal()
            
    def draw_tree(self, x, y):
        draw_node(x, y, self.data)
        if self.left:
            draw_edge(x, y, True)
            self.left.draw_tree(x-40,y-55)
        if self.right:
            draw_edge(x, y, False)
            self.right.draw_tree(x+40,y-55)

chars=[30,1,20,3,50,35,12]
root = None
for c in chars:
    if root is None:
        root = BinaryTreeNode(c)
    else:
        root.insert_tree(BinaryTreeNode(c))

root.tree_traversal()
print()
print(root.find_minimum().data)
  
x,y = 0,300
root.draw_tree(x, y)

hideturtle()
exitonclick()
done()