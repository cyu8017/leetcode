// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

using System;
using System.Collections.Generic;

public class Solution {
    public int RangeSum(int[] nums, int n, int left, int right) {
        var values = new List<int>();
        for (int i = 0; i < n; i++) {
            int total = 0;
            for (int j = i; j < n; j++) {
                total += nums[j];
                values.Add(total);
            }
        }
        values.Sort();
        long sum = 0;
        for (int i = left - 1; i < right; i++) sum += values[i];
        return (int)(sum % 1000000007);
    }
}
