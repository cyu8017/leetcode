// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<bool> CheckArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        var ans = new List<bool>();
        for (int t = 0; t < l.Length; t++) {
            var x = nums.Skip(l[t]).Take(r[t] - l[t] + 1).OrderBy(v => v).ToArray();
            if (x.Length < 3) { ans.Add(true); continue; }
            int diff = x[1] - x[0];
            bool ok = true;
            for (int i = 2; i < x.Length; i++) if (x[i] - x[i - 1] != diff) { ok = false; break; }
            ans.Add(ok);
        }
        return ans;
    }
}
