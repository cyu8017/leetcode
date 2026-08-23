// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) f[i] = new int[k + 1];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int h = 0; h <= k; h++) {
                for (int j = 0; j < i; j++) {
                    if (nums[i] == nums[j]) f[i][h] = Math.max(f[i][h], f[j][h]);
                    else if (h > 0) f[i][h] = Math.max(f[i][h], f[j][h - 1]);
                }
                f[i][h]++;
            }
            ans = Math.max(ans, f[i][k]);
        }
        return ans;
    }
}
