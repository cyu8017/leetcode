// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumTripletValue(int[] nums) {
        int n = nums.Length;
        int[] right = new int[n];
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = Math.Max(nums[i], right[i + 1]);
        var ts = new SortedSet<int>();
        ts.Add(nums[0]);
        int ans = 0;
        for (int j = 1; j < n - 1; j++) {
            if (right[j + 1] > nums[j]) {
                var view = ts.GetViewBetween(int.MinValue, nums[j] - 1);
                if (view.Count > 0) {
                    int it = view.Max;
                    ans = Math.Max(ans, it - nums[j] + right[j + 1]);
                }
            }
            ts.Add(nums[j]);
        }
        return ans;
    }
}
