// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

using System;
using System.Collections.Generic;

public class Solution {
    public int RobotSim(int[] commands, int[][] obstacles) {
        long Encode(int x, int y) => ((long)(x + 30000) << 20) | (uint)(y + 30000);
        var blocked = new HashSet<long>();
        foreach (var o in obstacles) blocked.Add(Encode(o[0], o[1]));
        int[][] dirs = { new[]{0,1}, new[]{1,0}, new[]{0,-1}, new[]{-1,0} };
        int x = 0, y = 0, d = 0, best = 0;
        foreach (int cmd in commands) {
            if (cmd == -1) d = (d + 1) % 4;
            else if (cmd == -2) d = (d + 3) % 4;
            else {
                int dx = dirs[d][0], dy = dirs[d][1];
                for (int step = 0; step < cmd; step++) {
                    int nx = x + dx, ny = y + dy;
                    if (blocked.Contains(Encode(nx, ny))) break;
                    x = nx; y = ny;
                }
                best = Math.Max(best, x * x + y * y);
            }
        }
        return best;
    }
}
