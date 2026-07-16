# LeetCode 0874 - Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        blocked = {(x, y) for x, y in obstacles}
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = d = best = 0
        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in blocked:
                        break
                    x, y = nx, ny
                best = max(best, x * x + y * y)
        return best
