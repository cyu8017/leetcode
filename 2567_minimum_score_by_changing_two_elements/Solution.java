// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

import java.util.Arrays;

class Solution {
    public int minimizeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int a = nums[n - 1] - nums[2];
        int b = nums[n - 3] - nums[0];
        int c = nums[n - 2] - nums[1];
        return Math.min(a, Math.min(b, c));
    }
}
