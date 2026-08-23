// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

using System;

public class Solution {
    public int MinimumPushes(string word) {
        int[] cnt = new int[26];
        foreach (char c in word) cnt[c - 'a']++;
        Array.Sort(cnt);
        int ans = 0;
        for (int i = 0; i < 26; i++) ans += (i / 8 + 1) * cnt[26 - i - 1];
        return ans;
    }
}
