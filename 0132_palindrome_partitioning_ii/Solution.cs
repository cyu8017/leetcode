// LeetCode 0132 - Palindrome Partitioning II
// https://leetcode.com/problems/palindrome-partitioning-ii/

using System;

public class Solution {
    public int MinCut(string s) {
        int n = s.Length;
        if (n == 0) return 0;
        var isPalindrome = new bool[n, n];
        for (int left = n - 1; left >= 0; left--)
            for (int right = left; right < n; right++)
                isPalindrome[left, right] = s[left] == s[right] && (right - left < 2 || isPalindrome[left + 1, right - 1]);
        var cuts = new int[n];
        for (int end = 0; end < n; end++) {
            cuts[end] = end;
            if (isPalindrome[0, end]) cuts[end] = 0;
            else for (int start = 0; start < end; start++)
                if (isPalindrome[start + 1, end]) cuts[end] = Math.Min(cuts[end], cuts[start] + 1);
        }
        return cuts[n - 1];
    }
}
