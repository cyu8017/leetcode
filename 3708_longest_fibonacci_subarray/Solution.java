// LeetCode 3708 - Longest Fibonacci Subarray
// https://leetcode.com/problems/longest-fibonacci-subarray/

class Solution {
    public int longestSubarray(int[] nums) {
        int f = 2, ans = f;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + nums[i - 2]) {
                f++;
                ans = Math.max(ans, f);
            } else f = 2;
        }
        return ans;
    }
}
