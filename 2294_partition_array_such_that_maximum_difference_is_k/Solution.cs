// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

using System;

public class Solution {
    public int PartitionArray(int[] nums, int k) {
        Array.Sort(nums);
        int ans = 1, start = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] - start > k) { ans++; start = nums[i]; }
        }
        return ans;
    }
}
