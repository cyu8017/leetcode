// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

using System;

public class Solution {
    public long MinCuttingCost(int n, int m, int k) {
        int x = Math.Max(n, m);
        if (x <= k) return 0;
        return 1L * k * (x - k);
    }
}
