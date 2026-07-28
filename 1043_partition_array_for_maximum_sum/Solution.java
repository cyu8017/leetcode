// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.length;
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int best = 0, limit = Math.min(k, i);
            for (int size = 1; size <= limit; size++) {
                best = Math.max(best, arr[i - size]);
                dp[i] = Math.max(dp[i], dp[i - size] + best * size);
            }
        }
        return dp[n];
    }
}
