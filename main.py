class BinarySearchTree:
  
    def __init__(self):
        self.root = None

    # Insert something into the tree.
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.insert(val)

    # Check if a value is in the tree.
    def contains(self, val):
        if self.root is None:
            return False
        else:
            return self.root.contains(val)

    def largest(self):
      if self.root is None:
        return False
      else:
        return self.root.largest()

    # Return all the items in the tree as a sorted list.
    def toList(self):
        if self.root is None:
            return []
        else:
            return self.root.toList()

    def depth(self):
      if self.root is None:
        return 0
      else:
        return self.root.depth()


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def getVal(self):
        return self.val

    def setVal(self, newVal):
        self.val = newVal

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, newLeft):
        self.left = newLeft

    def setRight(self, newRight):
        self.right = newRight

    # Insert something into the tree.
    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def contains(self, val):
      if self.val == val:
        return True
        
      if val < self.val:
        if self.left is None:
          return False
        else:
          return self.left.contains(val)

      else:
        if self.right is None:
          return False
        else:
          return self.right.contains(val)

    def largest(self):
        if self.right != None:
          return self.right.largest()
        return self.val

    def depth(self):
      if self and self.right and self.left != None:
          return max(self.right.depth(), self.left.depth()) + 1
      if self ==  None:
        return 0

      if self.left is None:
        return max(self.right.depth() + 1, 0)

      if self.right is None:
       return max(self.left.depth() + 1, 0)
        
    # Return all the items in the tree as a sorted list.
    def toList(self):
      if self.left is None:
        leftList = []
      else:
        leftList = self.left.toList()
        
      if self.right is None:
        rightList = []
      else:
        rightList = self.right.toList()
        
      return leftList + [self.val] + rightList

def main():
    s = input("Enter a list of numbers, seperated by spaces: ")
    lst = s.split()

    tree = BinarySearchTree()
    for x in lst:
        tree.insert(float(x))

    print(tree.depth())

    #print(tree.contains(3.0))


if __name__ == "__main__":
    main()
