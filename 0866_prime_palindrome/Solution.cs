// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

using System;

public class Solution {
    public int PrimePalindrome(int n) {
        bool IsPrime(int x) {
            if (x < 2) return false;
            if (x % 2 == 0) return x == 2;
            for (int d = 3; (long)d * d <= x; d += 2)
                if (x % d == 0) return false;
            return true;
        }
        if (n <= 2) return 2;
        if (n <= 3) return 3;
        if (n <= 5) return 5;
        if (n <= 7) return 7;
        if (n <= 11) return 11;
        for (int length = 1; length <= 5; length++) {
            int start = (int)Math.Pow(10, length - 1);
            int end = (int)Math.Pow(10, length);
            for (int root = start; root < end; root++) {
                string s = root.ToString();
                var pal = s;
                for (int i = s.Length - 2; i >= 0; i--) pal += s[i];
                int val = int.Parse(pal);
                if (val >= n && IsPrime(val)) return val;
            }
        }
        return 0;
    }
}
