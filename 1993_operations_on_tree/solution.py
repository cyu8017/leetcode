from typing import List

class LockingTree:
    def __init__(self, parent: List[int]):
        n = len(parent)
        self.locked = [-1] * n
        self.parent = parent
        self.children = [[] for _ in range(n)]
        for son, fa in enumerate(parent[1:], 1):
            self.children[fa].append(son)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        x = num
        while x != -1:
            if self.locked[x] != -1:
                return False
            x = self.parent[x]

        find = False

        def dfs(u: int) -> None:
            nonlocal find
            for v in self.children[u]:
                if self.locked[v] != -1:
                    self.locked[v] = -1
                    find = True
                dfs(v)

        dfs(num)
        if not find:
            return False
        self.locked[num] = user
        return True
