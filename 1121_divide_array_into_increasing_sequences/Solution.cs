// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

using System;
using System.Collections.Generic;

public class Solution {
    public bool CanDivideIntoSubsequences(int[] nums, int k) {
        var count = new Dictionary<int, int>();
        int maxFreq = 0;
        foreach (int x in nums) {
            if (!count.ContainsKey(x)) count[x] = 0;
            maxFreq = Math.Max(maxFreq, ++count[x]);
        }
        return nums.Length >= k * maxFreq;
    }
}
