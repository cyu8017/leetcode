// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

import java.util.*;

class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        Set<Long> blocked = new HashSet<>();
        for (int[] o : obstacles) blocked.add(encode(o[0], o[1]));
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0, y = 0, d = 0, best = 0;
        for (int cmd : commands) {
            if (cmd == -1) d = (d + 1) % 4;
            else if (cmd == -2) d = (d + 3) % 4;
            else {
                int dx = dirs[d][0], dy = dirs[d][1];
                for (int step = 0; step < cmd; step++) {
                    int nx = x + dx, ny = y + dy;
                    if (blocked.contains(encode(nx, ny))) break;
                    x = nx;
                    y = ny;
                }
                best = Math.max(best, x * x + y * y);
            }
        }
        return best;
    }

    private long encode(int x, int y) {
        return ((long) (x + 30000) << 20) | (y + 30000);
    }
}
