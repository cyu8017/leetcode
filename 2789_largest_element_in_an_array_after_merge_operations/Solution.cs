// LeetCode 2789 - Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

using System;

public class Solution {
    public long MaxArrayValue(int[] nums) {
        int n = nums.Length;
        long cur = nums[n - 1], ans = cur;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= cur) cur += nums[i];
            else cur = nums[i];
            ans = Math.Max(ans, cur);
        }
        return ans;
    }
}
