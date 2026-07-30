// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

using System;
using System.Collections.Generic;

public class Solution {
    public int WidestPairOfIndices(int[] nums1, int[] nums2) {
        var first = new Dictionary<int, int> { [0] = -1 };
        int ans = 0, s = 0;
        for (int i = 0; i < nums1.Length; i++) {
            s += nums1[i] - nums2[i];
            if (first.ContainsKey(s)) ans = Math.Max(ans, i - first[s]);
            else first[s] = i;
        }
        return ans;
    }
}