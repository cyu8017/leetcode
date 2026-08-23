// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindMissingElements(int[] nums) {
        int mn = 100, mx = 0;
        var s = new HashSet<int>();
        foreach (int x in nums) {
            mn = Math.Min(mn, x);
            mx = Math.Max(mx, x);
            s.Add(x);
        }
        var ans = new List<int>();
        for (int x = mn + 1; x < mx; x++) {
            if (!s.Contains(x)) ans.Add(x);
        }
        return ans.ToArray();
    }
}
