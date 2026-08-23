// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindOriginalArray(int[] changed) {
        if (changed.Length % 2 != 0) return Array.Empty<int>();
        Array.Sort(changed);
        var freq = new Dictionary<int, int>();
        foreach (int x in changed) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        var ans = new List<int>();
        foreach (int x in changed) {
            if (freq[x] == 0) continue;
            freq[x]--;
            if (!freq.ContainsKey(2 * x) || freq[2 * x] == 0) return Array.Empty<int>();
            freq[2 * x]--;
            ans.Add(x);
        }
        return ans.ToArray();
    }
}
