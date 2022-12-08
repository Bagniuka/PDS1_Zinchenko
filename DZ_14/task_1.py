class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, node):
        if self.id_node:
            if node < self.id_node:
                if self.left is None:
                    self.left = Tree(node)
                else:
                    self.left.insert(node)
            elif node > self.id_node:
                if self.right is None:
                    self.right = Tree(node)
                else:
                    self.right.insert(node)
        else:
            self.id_node = node

    def insert_list(self, list):
        for node in list:
            if self.id_node:
                if node < self.id_node:
                    if self.left is None:
                        self.left = Tree(node)
                    else:
                        self.left.insert(node)
                elif node > self.id_node:
                    if self.right is None:
                        self.right = Tree(node)
                    else:
                        self.right.insert(node)
            else:
                self.id_node = node

    # Findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

    # Find max value
    def find_max(self):
        if self.right:
            self.right.find_max()
        else:
            print(f'The max values is {self.id_node}')

    # Find min value
    def find_min(self):
        if self.left:
            self.left.find_min()
        else:
            print(f'The min value is {self.id_node}')

    # Function to find max value in the branch of minimum values to replace deleted node in case it has 2 children nodes
    def __max_in_min(self, iter_amm):
        if self.left and iter_amm == 0:
            self.left.__max_in_min(iter_amm=1)
        elif self.right and iter_amm == 1:
            self.right.__max_in_min(iter_amm=1)
        else:
            return self.id_node

    # Deleting node out of binary search tree (four possible variants)
    def delete_node(self, node):
        if node == self.id_node:
            if not self.right and not self.right:
                self.id_node = None
            if self.left and not self.right:
                self.id_node = self.left
            if self.right and not self.left:
                self.id_node = self.right
            if self.right and self.left:
                self.id_node = self.__max_in_min(0)
        else:
            if node > self.id_node:
                self.right.delete_node(node)
            if node < self.id_node:
                self.left.delete_node(node)


t1 = Tree(5)
my_list = [2, 1, 0, 3, 11, 9, 8, 10, 14, 12, 6, 13, 17]
t1.insert_list(my_list)
t1.print_tree()
t1.delete_node(2)
t1.print_tree()
