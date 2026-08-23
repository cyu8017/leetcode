// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

using System;

public class Solution {
    public string GetSmallestString(string s, int k) {
        char[] arr = s.ToCharArray();
        for (int i = 0; i < arr.Length; i++) {
            char c1 = arr[i];
            for (char c2 = 'a'; c2 < c1; c2++) {
                int d = Math.Min(c1 - c2, 26 - (c1 - c2));
                if (d <= k) {
                    arr[i] = c2;
                    k -= d;
                    break;
                }
            }
        }
        return new string(arr);
    }
}
