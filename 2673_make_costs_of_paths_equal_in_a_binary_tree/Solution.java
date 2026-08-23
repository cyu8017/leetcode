// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
    public int minIncrements(int n, int[] cost) {
        int ans = 0;
        for (int i = n / 2 - 1; i >= 0; i--) {
            int l = 2 * i + 1, r = 2 * i + 2;
            ans += Math.abs(cost[l] - cost[r]);
            cost[i] += Math.max(cost[l], cost[r]);
        }
        return ans;
    }
}
