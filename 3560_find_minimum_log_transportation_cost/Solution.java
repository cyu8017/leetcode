// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

class Solution {
    public long minCuttingCost(int n, int m, int k) {
        int x = Math.max(n, m);
        if (x <= k) return 0;
        return 1L * k * (x - k);
    }
}
