// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

using System;

public class Solution {
    public int MinSwaps(string s) {
        int bal = 0, mx = 0;
        foreach (char ch in s) {
            if (ch == '[') bal++;
            else bal--;
            mx = Math.Min(mx, bal);
        }
        return (-mx + 1) / 2;
    }
}