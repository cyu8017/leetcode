// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

using System;

using System.Text;

public class Solution {
    public string LargestPalindromic(string num) {
        int[] cnt = new int[10];
        foreach (char c in num) cnt[c - '0']++;
        var left = new StringBuilder();
        for (int d = 9; d >= 0; d--) {
            while (cnt[d] >= 2) {
                if (d == 0 && left.Length == 0) break;
                left.Append((char)('0' + d));
                cnt[d] -= 2;
            }
        }
        char mid = '\0';
        for (int d = 9; d >= 0; d--) {
            if (cnt[d] > 0) { mid = (char)('0' + d); break; }
        }
        if (left.Length == 0) {
            if (mid != '\0') return mid.ToString();
            return "0";
        }
        char[] leftChars = left.ToString().ToCharArray();
        Array.Reverse(leftChars);
        string right = new string(leftChars);
        if (mid != '\0') return left.ToString() + mid + right;
        return left.ToString() + right;
    }
}
