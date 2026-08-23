// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

class Solution {
    public int almostPalindromic(String s) {
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, Math.max(expand(s, i, i), expand(s, i, i + 1)));
        }
        return ans;
    }

    private int expand(String s, int l, int r) {
        int n = s.length();
        while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) { l--; r++; }
        int l1 = l - 1, r1 = r, l2 = l, r2 = r + 1;
        while (l1 >= 0 && r1 < n && s.charAt(l1) == s.charAt(r1)) { l1--; r1++; }
        while (l2 >= 0 && r2 < n && s.charAt(l2) == s.charAt(r2)) { l2--; r2++; }
        return Math.min(n, Math.max(r1 - l1 - 1, r2 - l2 - 1));
    }
}
