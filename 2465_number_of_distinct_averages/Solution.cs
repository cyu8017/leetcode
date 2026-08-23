// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

using System;
using System.Collections.Generic;

public class Solution {
    public int DistinctAverages(int[] nums) {
        Array.Sort(nums);
        var seen = new HashSet<int>();
        int l = 0, r = nums.Length - 1;
        while (l < r) {
            seen.Add(nums[l] + nums[r]);
            l++;
            r--;
        }
        return seen.Count;
    }
}
