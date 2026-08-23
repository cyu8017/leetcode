// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

using System;
using System.Collections.Generic;

public class Solution {
    public int NumEquivDominoPairs(int[][] dominoes) {
        var count = new Dictionary<int, int>();
        int ans = 0;
        foreach (var d in dominoes) {
            int key = Math.Min(d[0], d[1]) * 10 + Math.Max(d[0], d[1]);
            if (!count.ContainsKey(key)) count[key] = 0;
            ans += count[key]++;
        }
        return ans;
    }
}
