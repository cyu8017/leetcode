// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinDistinctFreqPair(int[] nums) {
        var cnt = new Dictionary<int, int>();
        foreach (int v in nums) {
            if (!cnt.ContainsKey(v)) cnt[v] = 0;
            cnt[v]++;
        }
        int x = nums[0];
        foreach (int v in nums) x = Math.Min(x, v);
        int minY = int.MaxValue;
        foreach (var y in cnt.Keys) {
            if (y < minY && cnt[x] != cnt[y]) minY = y;
        }
        if (minY == int.MaxValue) return new int[] { -1, -1 };
        return new int[] { x, minY };
    }
}
