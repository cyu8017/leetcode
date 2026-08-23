// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

using System;

public class Solution {
    public int MaximumLengthSubstring(string s) {
        int l = 0, ans = 0;
        int[] cnt = new int[26];
        for (int r = 0; r < s.Length; r++) {
            int idx = s[r] - 'a';
            cnt[idx]++;
            while (cnt[idx] > 2) {
                cnt[s[l] - 'a']--;
                l++;
            }
            ans = Math.Max(ans, r - l + 1);
        }
        return ans;
    }
}
