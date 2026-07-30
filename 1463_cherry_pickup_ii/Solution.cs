// LeetCode 1463 - Cherry Pickup Ii
// https://leetcode.com/problems/cherry-pickup-ii/

using System.Collections.Generic;
public class Solution {
    public int CherryPickup(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        var dp = new Dictionary<(int,int), int>();
        dp[(0, n - 1)] = grid[0][0] + (n > 1 ? grid[0][n - 1] : 0);
        for (int r = 1; r < m; r++) {
            var nxt = new Dictionary<(int,int), int>();
            foreach (var kv in dp) {
                int a = kv.Key.Item1, b = kv.Key.Item2, score = kv.Value;
                for (int na = a - 1; na <= a + 1; na++)
                    for (int nb = b - 1; nb <= b + 1; nb++)
                        if (na >= 0 && na < n && nb >= 0 && nb < n) {
                            int val = score + grid[r][na] + (na != nb ? grid[r][nb] : 0);
                            var key = (na, nb);
                            if (!nxt.ContainsKey(key) || val > nxt[key]) nxt[key] = val;
                        }
            }
            dp = nxt;
        }
        int ans = 0; foreach (int v in dp.Values) ans = System.Math.Max(ans, v); return ans;
    }
}
