from typing import List, Optional

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        width = max(1, n.bit_length())
        self.up = [parent[:]]
        for _ in range(1, width):
            prev = self.up[-1]
            self.up.append([-1 if p == -1 else prev[p] for p in prev])

    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0
        while k and node != -1:
            if k & 1:
                if bit >= len(self.up):
                    return -1
                node = self.up[bit][node]
            bit += 1
            k >>= 1
        return node
