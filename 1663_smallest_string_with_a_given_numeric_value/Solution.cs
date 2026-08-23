// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

using System;

public class Solution {
    public string GetSmallestString(int n, int k) {
        char[] a = new char[n];
        for (int i = 0; i < n; i++) a[i] = 'a';
        k -= n;
        for (int i = n - 1; i >= 0 && k > 0; i--) {
            int d = Math.Min(25, k);
            a[i] = (char)('a' + d);
            k -= d;
        }
        return new string(a);
    }
}
