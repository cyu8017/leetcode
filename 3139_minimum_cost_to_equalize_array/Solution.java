// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

class Solution {
    public int minCostToEqualizeArray(int[] nums, int cost1, int cost2) {
        final int MOD = 1_000_000_007;
        int n = nums.length;
        int minNum = nums[0], maxNum = nums[0];
        long sum = 0;
        for (int v : nums) {
            minNum = Math.min(minNum, v);
            maxNum = Math.max(maxNum, v);
            sum += v;
        }
        if (cost1 * 2L <= cost2 || n < 3) {
            long totalGap = 1L * maxNum * n - sum;
            return (int) (1L * cost1 * totalGap % MOD);
        }
        long ans = Long.MAX_VALUE;
        for (int target = maxNum; target < 2 * maxNum; target++) {
            int maxGap = target - minNum;
            long totalGap = 1L * target * n - sum;
            long pairs = totalGap / 2;
            long alt = totalGap - maxGap;
            if (alt < pairs) pairs = alt;
            long cost = 1L * cost1 * (totalGap - 2 * pairs) + 1L * cost2 * pairs;
            ans = Math.min(ans, cost);
        }
        return (int) (ans % MOD);
    }
}
