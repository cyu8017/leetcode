// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

using System;

public class Solution {
    public string SmallestNumber(string pattern) {
        int n = pattern.Length;
        char[] ans = new char[n + 1];
        for (int i = 0; i <= n; i++) ans[i] = (char)('1' + i);
        int i0 = 0;
        while (i0 < n) {
            if (pattern[i0] == 'I') { i0++; continue; }
            int j = i0;
            while (j < n && pattern[j] == 'D') j++;
            Array.Reverse(ans, i0, j - i0 + 1);
            i0 = j;
        }
        return new string(ans);
    }
}
