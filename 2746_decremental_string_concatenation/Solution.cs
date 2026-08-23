// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimizeConcatenatedLength(string[] words) {
        int n = words.Length;
        var memo = new Dictionary<(int, char, char), int>();
        int Dfs(int i, char first, char last) {
            if (i == n) return 0;
            var key = (i, first, last);
            if (memo.TryGetValue(key, out int cached)) return cached;
            string w = words[i];
            char wf = w[0], wl = w[w.Length - 1];
            int add1 = w.Length - (last == wf ? 1 : 0);
            int add2 = w.Length - (wl == first ? 1 : 0);
            int a = add1 + Dfs(i + 1, first, wl);
            int b = add2 + Dfs(i + 1, wf, last);
            return memo[key] = Math.Min(a, b);
        }
        string w0 = words[0];
        return w0.Length + Dfs(1, w0[0], w0[w0.Length - 1]);
    }
}
