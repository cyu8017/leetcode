// LeetCode 2574 - Left and Right Sum Differences
// https://leetcode.com/problems/left-and-right-sum-differences/

class Solution {
    public int[] leftRightDifference(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        int[] ans = new int[nums.length];
        int left = 0;
        for (int i = 0; i < nums.length; ++i) {
            int right = total - left - nums[i];
            ans[i] = Math.abs(left - right);
            left += nums[i];
        }
        return ans;
    }
}
