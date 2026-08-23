// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

class Solution {
    public int longestBalanced(String s) {
        int n = s.length(), ans = 0;
        for (int i = 0; i < n; i++) {
            int[] cnt = new int[26];
            int mx = 0, v = 0;
            for (int j = i; j < n; j++) {
                int c = s.charAt(j) - 'a';
                cnt[c]++;
                if (cnt[c] == 1) v++;
                mx = Math.max(mx, cnt[c]);
                if (mx * v == j - i + 1) ans = Math.max(ans, j - i + 1);
            }
        }
        return ans;
    }
}
