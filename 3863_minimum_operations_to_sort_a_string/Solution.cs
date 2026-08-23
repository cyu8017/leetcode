// LeetCode 3863 - Minimum Operations To Sort A String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

using System;

public class Solution {
    public int MinOperations(string s) {
        int n = s.Length;
        bool sorted = true;
        for (int i = 1; i < n; i++) {
            if (s[i] < s[i - 1]) { sorted = false; break; }
        }
        if (sorted) return 0;
        if (n == 2) return -1;
        char mn = s[0], mx = s[0];
        foreach (char c in s) { mn = c < mn ? c : mn; mx = c > mx ? c : mx; }
        if (s[0] == mn || s[n - 1] == mx) return 1;
        for (int i = 1; i < n - 1; i++) {
            if (s[i] == mn || s[i] == mx) return 2;
        }
        return 3;
    }
}
