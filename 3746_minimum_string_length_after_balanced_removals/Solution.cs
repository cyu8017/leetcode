// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

using System;

public class Solution {
    public int MinLengthAfterRemovals(string s) {
        int a = 0;
        foreach (char c in s) if (c == 'a') a++;
        int b = s.Length - a;
        return Math.Abs(a - b);
    }
}
