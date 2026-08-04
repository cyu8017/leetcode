// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

import java.util.*;

class Solution {
    private final Map<String, Integer> memo = new HashMap<>();
    public int minKnightMoves(int x, int y) {
        return dfs(Math.abs(x), Math.abs(y));
    }
    private int dfs(int a, int b) {
        if (a + b == 0) return 0;
        if (a + b == 2) return 2;
        String key = a + "," + b;
        if (memo.containsKey(key)) return memo.get(key);
        int ans = Math.min(dfs(Math.abs(a - 1), Math.abs(b - 2)), dfs(Math.abs(a - 2), Math.abs(b - 1))) + 1;
        memo.put(key, ans);
        return ans;
    }
}
