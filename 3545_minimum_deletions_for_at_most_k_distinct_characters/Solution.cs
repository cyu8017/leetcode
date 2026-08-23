// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

using System;

public class Solution {
    public int MinDeletion(string s, int k) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        Array.Sort(cnt);
        int ans = 0;
        for (int i = 0; i + k < 26; i++) ans += cnt[i];
        return ans;
    }
}
