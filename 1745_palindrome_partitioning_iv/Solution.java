// LeetCode 1745 - Palindrome Partitioning IV
// https://leetcode.com/problems/palindrome-partitioning-iv/

class Solution {
    public boolean checkPartitioning(String s) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                pal[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 2 || pal[i + 1][j - 1]);
            }
        }
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (pal[0][i] && pal[i + 1][j] && pal[j + 1][n - 1]) {
                    return true;
                }
            }
        }
        return false;
    }
}
