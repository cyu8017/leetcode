// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

using System;

public class Solution {
    public int MaxDistance(string[] words) {
        int n = words.Length, ans = 0;
        for (int i = 0; i < n; i++) {
            if (words[i] != words[0]) ans = Math.Max(ans, i + 1);
            if (words[i] != words[n - 1]) ans = Math.Max(ans, n - i);
        }
        return ans;
    }
}
