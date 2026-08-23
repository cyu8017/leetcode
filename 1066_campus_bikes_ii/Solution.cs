// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int AssignBikes(int[][] workers, int[][] bikes) {
        int m = bikes.Length;
        var memo = new Dictionary<(int, int), int>();

        int Dp(int i, int mask) {
            if (i == workers.Length) {
                return 0;
            }
            var key = (i, mask);
            if (memo.TryGetValue(key, out int cached)) {
                return cached;
            }
            int best = int.MaxValue;
            int wx = workers[i][0], wy = workers[i][1];
            for (int b = 0; b < m; b++) {
                if ((mask & (1 << b)) != 0) {
                    continue;
                }
                int dist = Math.Abs(wx - bikes[b][0]) + Math.Abs(wy - bikes[b][1]);
                best = Math.Min(best, dist + Dp(i + 1, mask | (1 << b)));
            }
            memo[key] = best;
            return best;
        }

        return Dp(0, 0);
    }
}
