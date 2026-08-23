// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

using System;

public class Solution {
    public int PartitionDisjoint(int[] nums) {
        int n = nums.Length;
        int[] minRight = new int[n];
        minRight[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) minRight[i] = Math.Min(nums[i], minRight[i + 1]);
        int maxLeft = nums[0];
        for (int i = 1; i < n; i++) {
            if (maxLeft <= minRight[i]) return i;
            maxLeft = Math.Max(maxLeft, nums[i]);
        }
        return n - 1;
    }
}
