// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

import java.util.Arrays;

class Solution {
    public int minDeletion(String s, int k) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        Arrays.sort(cnt);
        int ans = 0;
        for (int i = 0; i + k < 26; i++) ans += cnt[i];
        return ans;
    }
}
