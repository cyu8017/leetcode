class FindElements:
    def __init__(self, root):
        if isinstance(root, list):
            class Node:
                def __init__(self, val):
                    self.val, self.left, self.right = val, None, None
            nodes = [None if value is None else Node(value) for value in root]
            children = iter(nodes[1:])
            for node in nodes:
                if node is not None:
                    node.left = next(children, None)
                    node.right = next(children, None)
            root = nodes[0] if nodes else None
        self.values = set()
        def recover(node, value):
            if not node:
                return
            node.val = value
            self.values.add(value)
            recover(node.left, 2 * value + 1)
            recover(node.right, 2 * value + 2)
        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
