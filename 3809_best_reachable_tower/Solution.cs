// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

using System;

public class Solution {
    public int[] BestTower(int[][] towers, int[] center, int radius) {
        int cx = center[0], cy = center[1];
        int idx = -1;
        for (int i = 0; i < towers.Length; i++) {
            int x = towers[i][0], y = towers[i][1], q = towers[i][2];
            int dist = Math.Abs(x - cx) + Math.Abs(y - cy);
            if (dist > radius) continue;
            if (idx == -1 || towers[idx][2] < q ||
                (towers[idx][2] == q &&
                 (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1])))) {
                idx = i;
            }
        }
        if (idx == -1) return new int[] { -1, -1 };
        return new int[] { towers[idx][0], towers[idx][1] };
    }
}
