class Solution:
    def displayTable(self, orders):
        foods = sorted({food for _, _, food in orders})
        tables = sorted({int(table) for _, table, _ in orders})
        counts = {}
        for _, table, food in orders:
            counts[int(table), food] = counts.get((int(table), food), 0) + 1
        return [["Table"] + foods] + [[str(table)] + [str(counts.get((table, food), 0)) for food in foods]
                                      for table in tables]
