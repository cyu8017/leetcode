// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

import java.util.Arrays;

class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        int n = nums.length;
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) { arr[i][0] = nums[i]; arr[i][1] = i; }
        Arrays.sort(arr, (a, b) -> Integer.compare(b[0], a[0]));
        int[] idx = new int[k];
        for (int i = 0; i < k; i++) idx[i] = arr[i][1];
        Arrays.sort(idx);
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) ans[i] = nums[idx[i]];
        return ans;
    }
}
