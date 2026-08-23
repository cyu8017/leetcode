// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

// JavaScript problem; C# stand-in.
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public Func<int[], int> MemoizeII(Func<int[], int> fn) {
        var cache = new Dictionary<string, int>();
        return args => {
            var sb = new StringBuilder();
            foreach (int a in args) { sb.Append('|'); sb.Append(a); }
            string k = sb.ToString();
            if (cache.TryGetValue(k, out int v)) return v;
            v = fn(args);
            cache[k] = v;
            return v;
        };
    }
}
