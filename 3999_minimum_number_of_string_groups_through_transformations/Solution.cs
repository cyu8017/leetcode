// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    static int LeastRotation(string s) {
        int n = s.Length;
        int i = 0, j = 1, k = 0;
        while (i < n && j < n && k < n) {
            char a = s[(i + k) % n];
            char b = s[(j + k) % n];
            if (a == b) ++k;
            else {
                if (a > b) i += k + 1;
                else j += k + 1;
                if (i == j) ++j;
                k = 0;
            }
        }
        return i < j ? i : j;
    }

    static string CanonicalRotate(string s) {
        int n = s.Length;
        if (n <= 1) return s;
        int r = LeastRotation(s);
        if (r == 0) return s;
        return s.Substring(r) + s.Substring(0, r);
    }

    public int MinimumGroups(string[] words) {
        var keys = new List<string>(words.Length);
        foreach (string w in words) {
            int n = w.Length;
            var even = new StringBuilder();
            var odd = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0) even.Append(w[i]);
                else odd.Append(w[i]);
            }
            string e = CanonicalRotate(even.ToString());
            string o = CanonicalRotate(odd.ToString());
            keys.Add(e + "#" + o);
        }
        keys.Sort(StringComparer.Ordinal);
        int groups = 0;
        for (int i = 0; i < keys.Count; i++) {
            if (i == 0 || keys[i] != keys[i - 1]) ++groups;
        }
        return groups;
    }
}
