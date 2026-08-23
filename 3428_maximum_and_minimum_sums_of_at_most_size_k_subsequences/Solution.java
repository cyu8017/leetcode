// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

import java.util.Arrays;

class Solution {
    public int minMaxSums(int[] nums, int k) {
        final int mod = 1_000_000_007;
        Arrays.sort(nums);
        int n = nums.length;
        int[][] C = new int[n + 1][k];
        for (int i = 0; i <= n; i++) {
            C[i][0] = 1;
            for (int j = 1; j < k && j <= i; j++) C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int waysMax = 0;
            for (int j = 0; j < k && j <= i; j++) waysMax = (waysMax + C[i][j]) % mod;
            int waysMin = 0;
            int right = n - i - 1;
            for (int j = 0; j < k && j <= right; j++) waysMin = (waysMin + C[right][j]) % mod;
            ans = (int) ((ans + (long) nums[i] * waysMax % mod + (long) nums[i] * waysMin % mod) % mod);
        }
        return ans;
    }
}
