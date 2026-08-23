// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumDeletions(string word, int k) {
        int[] freq = new int[26];
        foreach (char c in word) freq[c - 'a']++;
        var nums = new List<int>();
        foreach (int v in freq) if (v > 0) nums.Add(v);
        int F(int v) {
            int ans = 0;
            foreach (int x in nums) {
                if (x < v) ans += x;
                else if (x > v + k) ans += x - v - k;
            }
            return ans;
        }
        int ans = word.Length;
        for (int i = 0; i <= word.Length; i++) ans = Math.Min(ans, F(i));
        return ans;
    }
}
