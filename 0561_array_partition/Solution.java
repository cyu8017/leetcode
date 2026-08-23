// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

import java.util.Arrays;

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int total = 0;
        for (int i = 0; i < nums.length; i += 2) {
            total += nums[i];
        }
        return total;
    }
}
