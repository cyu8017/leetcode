// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

using System;
using System.Collections.Generic;

public class Solution {
    public int LargestUniqueNumber(int[] nums) {
        var count = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        int ans = -1;
        foreach (var kv in count) {
            if (kv.Value == 1) ans = Math.Max(ans, kv.Key);
        }
        return ans;
    }
}
