class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def inOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                minValue = self.right.findMin()
                self.data = minValue
                self.right = self.right.delete(minValue)

        return self

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()

def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    numbersTree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbersTree.delete(20)
    print('After deleting 20:', numbersTree.inOrderTraversal()) # [1, 4, 9, 17, 18, 23, 34]

    numbersTree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbersTree.delete(9)
    print('After deleting 9:', numbersTree.inOrderTraversal())  # [1, 4, 17, 18, 20, 23, 34]

    numbersTree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbersTree.delete(17)
    print('After deleting 17:', numbersTree.inOrderTraversal())  # [1, 4, 9, 18, 20, 23, 34]
    