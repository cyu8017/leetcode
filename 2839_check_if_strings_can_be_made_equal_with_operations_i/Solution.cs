// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

using System;

public class Solution {
    public bool CanBeEqual(string s1, string s2) {
        char[] a = { s1[0], s1[2] }, b = { s2[0], s2[2] }, c = { s1[1], s1[3] }, d = { s2[1], s2[3] };
        Array.Sort(a); Array.Sort(b); Array.Sort(c); Array.Sort(d);
        return a[0] == b[0] && a[1] == b[1] && c[0] == d[0] && c[1] == d[1];
    }
}
