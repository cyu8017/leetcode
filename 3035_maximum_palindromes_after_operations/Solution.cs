// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

using System;

public class Solution {
    static int Popcount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }

    public int MaxPalindromesAfterOperations(string[] words) {
        int s = 0, mask = 0;
        foreach (var w in words) {
            s += w.Length;
            foreach (char c in w) mask ^= 1 << (c - 'a');
        }
        s -= Popcount(mask);
        Array.Sort(words, (a, b) => a.Length.CompareTo(b.Length));
        int ans = 0;
        foreach (var w in words) {
            s -= w.Length / 2 * 2;
            if (s < 0) break;
            ans++;
        }
        return ans;
    }
}
