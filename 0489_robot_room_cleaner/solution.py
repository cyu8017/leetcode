# LeetCode 0489 - Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/

class Solution:
    def cleanRoom(self, robot) -> None:
        visited: set[tuple[int, int, int]] = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def backtrack(row: int, col: int, direction: int) -> None:
            robot.clean()
            for step in range(4):
                d = (direction + step) % 4
                dr, dc = directions[d]
                next_row, next_col = row + dr, col + dc
                if (next_row, next_col, d) not in visited and robot.move():
                    visited.add((next_row, next_col, d))
                    backtrack(next_row, next_col, d)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        visited.add((0, 0, 0))
        backtrack(0, 0, 0)
