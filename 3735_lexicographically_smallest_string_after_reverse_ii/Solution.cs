// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

using System;

public class Solution {
    public string LexSmallest(string s) {
        int n = s.Length;
        string best = s;
        for (int i = 1; i <= n; i++) {
            char[] t = s.ToCharArray();
            Array.Reverse(t, 0, i);
            string ts = new string(t);
            if (string.CompareOrdinal(ts, best) < 0) best = ts;
        }
        for (int i = 0; i < n; i++) {
            char[] t = s.ToCharArray();
            Array.Reverse(t, i, n - i);
            string ts = new string(t);
            if (string.CompareOrdinal(ts, best) < 0) best = ts;
        }
        return best;
    }
}
