// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int FindShortestSubArray(int[] nums) {
        var first = new Dictionary<int, int>();
        var last = new Dictionary<int, int>();
        var count = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (!first.ContainsKey(nums[i])) first[nums[i]] = i;
            last[nums[i]] = i;
            if (!count.ContainsKey(nums[i])) count[nums[i]] = 0;
            count[nums[i]]++;
        }
        int degree = 0;
        foreach (var freq in count.Values) degree = Math.Max(degree, freq);
        int best = int.MaxValue;
        foreach (var kv in count) {
            if (kv.Value == degree) best = Math.Min(best, last[kv.Key] - first[kv.Key] + 1);
        }
        return best;
    }
}
