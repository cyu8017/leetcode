// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

using System;

public class Solution {
    public int CountBinarySubstrings(string s) {
        int prev = 0, cur = 1, ans = 0;
        for (int i = 1; i < s.Length; i++) {
            if (s[i] == s[i - 1]) cur++;
            else {
                ans += Math.Min(prev, cur);
                prev = cur;
                cur = 1;
            }
        }
        return ans + Math.Min(prev, cur);
    }
}
