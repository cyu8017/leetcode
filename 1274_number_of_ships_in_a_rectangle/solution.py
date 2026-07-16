class Sea:
    def hasShips(self, topRight: "Point", bottomLeft: "Point") -> bool: ...

class Solution:
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        tx, ty = topRight
        bx, by = bottomLeft
        if tx < bx or ty < by or not sea.hasShips(topRight, bottomLeft):
            return 0
        if tx == bx and ty == by:
            return 1
        mx, my = (tx + bx) // 2, (ty + by) // 2
        return (
            self.countShips(sea, [mx, my], [bx, by])
            + self.countShips(sea, [tx, my], [mx + 1, by])
            + self.countShips(sea, [mx, ty], [bx, my + 1])
            + self.countShips(sea, [tx, ty], [mx + 1, my + 1])
        )
