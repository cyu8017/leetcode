// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

import java.util.*;

class Solution {
    public int minDays(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        return dp(n, memo);
    }

    private int dp(int x, Map<Integer, Integer> memo) {
        if (x <= 1) {
            return x;
        }
        if (memo.containsKey(x)) {
            return memo.get(x);
        }
        int a = x % 2 + dp(x / 2, memo);
        int b = x % 3 + dp(x / 3, memo);
        int result = 1 + Math.min(a, b);
        memo.put(x, result);
        return result;
    }
}
