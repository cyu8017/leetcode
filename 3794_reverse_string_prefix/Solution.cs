// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

using System;

public class Solution {
    public string ReversePrefix(string s, int k) {
        char[] arr = s.ToCharArray();
        Array.Reverse(arr, 0, k);
        return new string(arr);
    }
}
