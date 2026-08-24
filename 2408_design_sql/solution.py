# LeetCode 2408 - Design SQL
# https://leetcode.com/problems/design-sql/

from typing import List


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        self.nextID = {}
        for name in names:
            self.tables[name] = []
            self.nextID[name] = 1

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables:
            return False
        row_id = self.nextID[name]
        self.nextID[name] = row_id + 1
        full = [str(row_id)] + list(row)
        self.tables[name].append(full)
        return True

    def rmv(self, name: str, rowId: int) -> None:
        rows = self.tables[name]
        for i in range(len(rows)):
            if int(rows[i][0]) == rowId:
                rows.pop(i)
                return

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        for r in self.tables[name]:
            if int(r[0]) == rowId:
                if columnId < 1 or columnId >= len(r):
                    return "<null>"
                return r[columnId]
        return "<null>"

    def exp(self, name: str) -> List[str]:
        return [",".join(r) for r in self.tables[name]]
