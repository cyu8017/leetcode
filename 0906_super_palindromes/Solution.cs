// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

using System;

public class Solution {
    public int SuperpalindromesInRange(string left, string right) {
        long L = long.Parse(left), R = long.Parse(right);
        int ans = 0;
        bool IsPal(long x) {
            string s = x.ToString();
            int n = s.Length;
            for (int i = 0; i < n / 2; i++) if (s[i] != s[n - 1 - i]) return false;
            return true;
        }
        for (long k = 1; k <= 100000; k++) {
            string s = k.ToString();
            char[] revArr = s.ToCharArray();
            Array.Reverse(revArr);
            long pal = long.Parse(s + new string(revArr));
            long sq = pal * pal;
            if (sq > R) break;
            if (sq >= L && IsPal(sq)) ans++;
        }
        for (long k = 1; k <= 100000; k++) {
            string s = k.ToString();
            string rev = s.Substring(0, s.Length - 1);
            char[] revArr = rev.ToCharArray();
            Array.Reverse(revArr);
            long pal = long.Parse(s + new string(revArr));
            long sq = pal * pal;
            if (sq > R) break;
            if (sq >= L && IsPal(sq)) ans++;
        }
        return ans;
    }
}
