// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

public class Solution {
    public int MaxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.Length;
        var dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int best = 0;
            for (int size = 1; size <= Math.Min(k, i); size++) {
                best = Math.Max(best, arr[i - size]);
                dp[i] = Math.Max(dp[i], dp[i - size] + best * size);
            }
        }
        return dp[n];
    }
}
