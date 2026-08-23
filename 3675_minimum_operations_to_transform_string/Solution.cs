// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

using System;

public class Solution {
    public int MinOperations(string s) {
        int ans = 0;
        foreach (char c in s) {
            if (c != 'a') ans = Math.Max(ans, 26 - (c - 'a'));
        }
        return ans;
    }
}
