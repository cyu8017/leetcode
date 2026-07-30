// LeetCode 1433 - Check If A String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

using System;
public class Solution {
    public bool CheckIfCanBreak(string s1, string s2) {
        char[] a = s1.ToCharArray(), b = s2.ToCharArray();
        Array.Sort(a); Array.Sort(b);
        bool ge = true, le = true;
        for (int i = 0; i < a.Length; i++) { if (a[i] < b[i]) ge = false; if (a[i] > b[i]) le = false; }
        return ge || le;
    }
}
