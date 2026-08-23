// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

import java.util.*;

class Solution {
    private int x;
    private Map<Integer, Integer> memo = new HashMap<>();

    public int leastOpsExpressTarget(int x, int target) {
        this.x = x;
        return dfs(target);
    }

    private int dfs(int t) {
        if (memo.containsKey(t)) return memo.get(t);
        if (x > t) {
            int ans = Math.min(2 * t - 1, 2 * (x - t));
            memo.put(t, ans);
            return ans;
        }
        if (x == t) {
            memo.put(t, 0);
            return 0;
        }
        long prod = x;
        int n = 0;
        while (prod < t) {
            prod *= x;
            n++;
        }
        if (prod == t) {
            memo.put(t, n);
            return n;
        }
        int ans = dfs(t - (int) (prod / x)) + n;
        if (prod < 2L * t) ans = Math.min(ans, dfs((int) prod - t) + n + 1);
        memo.put(t, ans);
        return ans;
    }
}
