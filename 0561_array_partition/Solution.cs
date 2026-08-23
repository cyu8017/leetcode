// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

using System;

public class Solution {
    public int ArrayPairSum(int[] nums) {
        Array.Sort(nums);
        int total = 0;
        for (int i = 0; i < nums.Length; i += 2) total += nums[i];
        return total;
    }
}
