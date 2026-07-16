from typing import List

from collections import defaultdict

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()
    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        order = []
        def visit(name):
            if name not in self.dead:
                order.append(name)
            for child in self.children[name]:
                visit(child)
        visit(self.king)
        return order
