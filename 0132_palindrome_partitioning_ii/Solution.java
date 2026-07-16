// LeetCode 0132 - Palindrome Partitioning II
// https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution {
    public int minCut(String s) {
        int n = s.length();
        if (n == 0) return 0;
        boolean[][] isPalindrome = new boolean[n][n];
        for (int left = n - 1; left >= 0; left--) {
            for (int right = left; right < n; right++) {
                isPalindrome[left][right] = s.charAt(left) == s.charAt(right)
                    && (right - left < 2 || isPalindrome[left + 1][right - 1]);
            }
        }
        int[] cuts = new int[n];
        for (int end = 0; end < n; end++) {
            cuts[end] = end;
            if (isPalindrome[0][end]) {
                cuts[end] = 0;
            } else {
                for (int start = 0; start < end; start++) {
                    if (isPalindrome[start + 1][end]) cuts[end] = Math.min(cuts[end], cuts[start] + 1);
                }
            }
        }
        return cuts[n - 1];
    }
}
