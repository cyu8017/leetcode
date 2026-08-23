// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int maximizeTheProfit(int n, List<List<Integer>> offers) {
        var byEnd = new ArrayList<List<Integer>>[n];
        for (int i = 0; i < n; i++) byEnd.set(i, new ArrayList<List<Integer>>());
        for (var o : offers) byEnd.get(o[1]).add(o);
        int[] dp = new int[n + 1];
        for (int end = 0; end < n; end++) {
            dp[end + 1] = dp[end];
            for (var o : byEnd.get(end))
                dp[end + 1] = Math.max(dp[end + 1], dp[o[0]] + o[2]);
        }
        return dp[n];
    }
}
