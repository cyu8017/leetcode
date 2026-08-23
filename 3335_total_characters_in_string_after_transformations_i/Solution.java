// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

class Solution {
    public int lengthAfterTransformations(String s, int t) {
        final int mod = 1_000_000_007;
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        for (int step = 0; step < t; step++) {
            int[] ncnt = new int[26];
            for (int i = 0; i < 25; i++) ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod;
            ncnt[0] = (ncnt[0] + cnt[25]) % mod;
            ncnt[1] = (ncnt[1] + cnt[25]) % mod;
            cnt = ncnt;
        }
        int ans = 0;
        for (int v : cnt) ans = (ans + v) % mod;
        return ans;
    }
}
