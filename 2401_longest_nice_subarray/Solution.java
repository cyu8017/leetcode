// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

class Solution {
    public int longestNiceSubarray(int[] nums) {
        int used = 0, left = 0, ans = 0;
        for (int right = 0; right < nums.length; right++) {
            while ((used & nums[right]) != 0) {
                used ^= nums[left];
                left++;
            }
            used |= nums[right];
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
