// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution {
    public int longestSubarray(int[] nums) {
        int mx = nums[0];
        for (int x : nums) if (x > mx) mx = x;
        int ans = 0, cur = 0;
        for (int x : nums) {
            if (x == mx) {
                cur++;
                ans = Math.max(ans, cur);
            } else {
                cur = 0;
            }
        }
        return ans;
    }
}
