// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

class Solution {
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        int[] left = new int[n], right = new int[n];
        for (int i = 0; i < n; i++) { left[i] = 1; right[i] = 1; }
        for (int i = 1; i < n; i++) {
            if (nums[i] >= nums[i - 1]) left[i] = left[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1;
        }
        int ans = 0;
        for (int v : left) ans = Math.max(ans, v);
        for (int i = 0; i < n; i++) {
            int a = i > 0 ? left[i - 1] : 0;
            int b = i + 1 < n ? right[i + 1] : 0;
            if (i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]) {
                ans = Math.max(ans, Math.max(a + 1, b + 1));
            } else {
                ans = Math.max(ans, a + b + 1);
            }
        }
        return ans;
    }
}
