// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

using System;

public class Solution {
    public int FindMinimumOperations(string s1, string s2, string s3) {
        int n = Math.Min(s1.Length, Math.Min(s2.Length, s3.Length));
        int i = 0;
        while (i < n && s1[i] == s2[i] && s2[i] == s3[i]) i++;
        if (i == 0) return -1;
        return s1.Length + s2.Length + s3.Length - 3 * i;
    }
}
