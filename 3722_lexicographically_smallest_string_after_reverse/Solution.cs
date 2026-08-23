// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

using System;

public class Solution {
    public string LexSmallest(string s) {
        string ans = s;
        int n = s.Length;
        for (int k = 1; k <= n; k++) {
            char[] a1 = s.ToCharArray();
            Array.Reverse(a1, 0, k);
            string t1 = new string(a1);
            char[] a2 = s.ToCharArray();
            Array.Reverse(a2, n - k, k);
            string t2 = new string(a2);
            if (string.CompareOrdinal(t1, ans) < 0) ans = t1;
            if (string.CompareOrdinal(t2, ans) < 0) ans = t2;
        }
        return ans;
    }
}
