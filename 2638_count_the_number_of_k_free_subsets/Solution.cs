// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

using System;
using System.Collections.Generic;

public class Solution {
    public long CountTheNumOfKFreeSubsets(int[] nums, int k) {
        Array.Sort(nums);
        var groups = new Dictionary<int, List<int>>();
        foreach (int x in nums) {
            int key = x % k;
            if (!groups.ContainsKey(key)) groups[key] = new List<int>();
            groups[key].Add(x);
        }
        long ans = 1;
        foreach (var g in groups.Values) {
            int prevVal = -1;
            long prevTake = 0, prevSkip = 1;
            foreach (int v in g) {
                long take = 0, skip = prevTake + prevSkip;
                if (prevVal + k == v) take = prevSkip;
                else take = prevTake + prevSkip;
                prevTake = take;
                prevSkip = skip;
                prevVal = v;
            }
            ans *= prevTake + prevSkip;
        }
        return ans;
    }
}
