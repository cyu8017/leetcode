// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

import java.util.Arrays;

class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int max = 0;
        int half = nums.length / 2;
        for (int i = 0; i < half; i++) {
            max = Math.max(max, nums[i] + nums[nums.length - 1 - i]);
        }
        return max;
    }
}
