class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right
    def evaluate(self):
        if self.val not in "+-*/": return int(self.val)
        a, b = self.left.evaluate(), self.right.evaluate()
        return {"+": lambda: a+b, "-": lambda: a-b, "*": lambda: a*b, "/": lambda: int(a/b)}[self.val]()
    def __eq__(self, other): return self.evaluate() == other
    def __repr__(self): return str(self.evaluate())
class TreeBuilder:
    def expTree(self, postfix):
        stack = []
        for token in postfix:
            node = Node(token)
            if token in "+-*/": node.right = stack.pop(); node.left = stack.pop()
            stack.append(node)
        return stack[-1]
