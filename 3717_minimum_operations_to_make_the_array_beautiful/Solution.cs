// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        var f = new Dictionary<int, int> { [nums[0]] = 0 };
        for (int i = 1; i < nums.Length; i++) {
            int x = nums[i];
            var g = new Dictionary<int, int>();
            foreach (var kv in f) {
                int pre = kv.Key, s = kv.Value;
                int cur = (x + pre - 1) / pre * pre;
                while (cur <= 100) {
                    int val = s + (cur - x);
                    if (!g.ContainsKey(cur) || g[cur] > val) g[cur] = val;
                    cur += pre;
                }
            }
            f = g;
        }
        int ans = int.MaxValue;
        foreach (var v in f.Values) ans = Math.Min(ans, v);
        return ans;
    }
}
