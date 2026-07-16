// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

using System;
using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<string, bool> memo = new Dictionary<string, bool>();

    public bool IsScramble(string s1, string s2) {
        string key = s1 + "#" + s2;
        if (memo.ContainsKey(key)) {
            return memo[key];
        }
        if (s1 == s2) {
            memo[key] = true;
            return true;
        }
        char[] a = s1.ToCharArray();
        char[] b = s2.ToCharArray();
        Array.Sort(a);
        Array.Sort(b);
        if (new string(a) != new string(b)) {
            memo[key] = false;
            return false;
        }

        int n = s1.Length;
        for (int i = 1; i < n; i++) {
            if (IsScramble(s1.Substring(0, i), s2.Substring(0, i))
                    && IsScramble(s1.Substring(i), s2.Substring(i))) {
                memo[key] = true;
                return true;
            }
            if (IsScramble(s1.Substring(0, i), s2.Substring(n - i))
                    && IsScramble(s1.Substring(i), s2.Substring(0, n - i))) {
                memo[key] = true;
                return true;
            }
        }
        memo[key] = false;
        return false;
    }
}
