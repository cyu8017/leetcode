// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

using System;
using System.Collections.Generic;

public class Solution {
    public int LeastOpsExpressTarget(int x, int target) {
        var memo = new Dictionary<int, int>();
        int Dfs(int t) {
            if (memo.ContainsKey(t)) return memo[t];
            if (x > t) return memo[t] = Math.Min(2 * t - 1, 2 * (x - t));
            if (x == t) return memo[t] = 0;
            long prod = x;
            int n = 0;
            while (prod < t) {
                prod *= x;
                n++;
            }
            if (prod == t) return memo[t] = n;
            int ans = Dfs(t - (int)(prod / x)) + n;
            if (prod < 2L * t) ans = Math.Min(ans, Dfs((int)prod - t) + n + 1);
            return memo[t] = ans;
        }
        return Dfs(target);
    }
}
