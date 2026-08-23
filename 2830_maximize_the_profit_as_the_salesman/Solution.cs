// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximizeTheProfit(int n, IList<IList<int>> offers) {
        var byEnd = new List<IList<int>>[n];
        for (int i = 0; i < n; i++) byEnd[i] = new List<IList<int>>();
        foreach (var o in offers) byEnd[o[1]].Add(o);
        int[] dp = new int[n + 1];
        for (int end = 0; end < n; end++) {
            dp[end + 1] = dp[end];
            foreach (var o in byEnd[end])
                dp[end + 1] = Math.Max(dp[end + 1], dp[o[0]] + o[2]);
        }
        return dp[n];
    }
}
