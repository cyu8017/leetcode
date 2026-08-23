// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution {
    public int[] minCosts(int[] cost) {
        int n = cost.length;
        int[] ans = new int[n];
        int mi = cost[0];
        for (int i = 0; i < n; i++) {
            mi = Math.min(mi, cost[i]);
            ans[i] = mi;
        }
        return ans;
    }
}
