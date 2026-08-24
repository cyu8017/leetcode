# LeetCode 3484 - Design Spreadsheet
# https://leetcode.com/problems/design-spreadsheet/


class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        if formula and formula[0] == "=":
            formula = formula[1:]
        total = 0
        start = 0
        while start < len(formula):
            plus = formula.find("+", start)
            p = formula[start:] if plus < 0 else formula[start:plus]
            is_num = bool(p) and ((p[0] >= "0" and p[0] <= "9") or (p[0] == "-" and len(p) > 1))
            if is_num:
                for i in range(1, len(p)):
                    if p[i] < "0" or p[i] > "9":
                        is_num = False
                        break
            if is_num:
                total += int(p)
            else:
                total += self.cells.get(p, 0)
            if plus < 0:
                break
            start = plus + 1
        return total
