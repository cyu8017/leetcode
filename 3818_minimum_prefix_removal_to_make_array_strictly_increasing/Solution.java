// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

class Solution {
    public int minimumPrefixLength(int[] nums) {
        for (int i = nums.length - 1; i > 0; i--) {
            if (nums[i - 1] >= nums[i]) return i;
        }
        return 0;
    }
}
