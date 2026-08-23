// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

using System;

public class Solution {
    public string MakeSmallestPalindrome(string s) {
        char[] arr = s.ToCharArray();
        int n = arr.Length;
        for (int i = 0; i < n / 2; i++) {
            char c = (char)Math.Min(arr[i], arr[n - 1 - i]);
            arr[i] = arr[n - 1 - i] = c;
        }
        return new string(arr);
    }
}
