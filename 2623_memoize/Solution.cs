// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

// JavaScript problem; C# stand-in.
using System;
using System.Collections.Generic;

public class Solution {
    public Func<int, int> Memoize(Func<int, int> fn) {
        var cache = new Dictionary<int, int>();
        return x => {
            if (cache.TryGetValue(x, out int v)) return v;
            v = fn(x);
            cache[x] = v;
            return v;
        };
    }
}
