class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x0, y0 = coordinates[0]
        dx, dy = coordinates[1][0] - x0, coordinates[1][1] - y0
        return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates[2:])
