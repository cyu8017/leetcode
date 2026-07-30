// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinKnightMoves(int x, int y) {
        x = Math.Abs(x);
        y = Math.Abs(y);
        var memo = new Dictionary<(int, int), int>();

        int Dfs(int a, int b) {
            if (a + b == 0) return 0;
            if (a + b == 2) return 2;
            var key = (a, b);
            if (memo.TryGetValue(key, out int cached)) return cached;
            int ans = Math.Min(Dfs(Math.Abs(a - 1), Math.Abs(b - 2)), Dfs(Math.Abs(a - 2), Math.Abs(b - 1))) + 1;
            memo[key] = ans;
            return ans;
        }

        return Dfs(x, y);
    }
}
