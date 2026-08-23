// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinLengthAfterRemovals(IList<int> nums) {
        int n = nums.Count, mx = 0;
        var freq = new Dictionary<int, int>();
        foreach (int v in nums) {
            if (!freq.ContainsKey(v)) freq[v] = 0;
            mx = Math.Max(mx, ++freq[v]);
        }
        if (mx <= n / 2) return n % 2;
        return 2 * mx - n;
    }
}
