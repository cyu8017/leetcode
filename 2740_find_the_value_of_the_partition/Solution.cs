// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

using System;

public class Solution {
    public int FindValueOfPartition(int[] nums) {
        Array.Sort(nums);
        int ans = int.MaxValue;
        for (int i = 1; i < nums.Length; i++)
            ans = Math.Min(ans, nums[i] - nums[i - 1]);
        return ans;
    }
}
