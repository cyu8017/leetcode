// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

class Solution {
    public int countSubstrings(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); ++i) {
            total += expand(s, i, i);
            total += expand(s, i, i + 1);
        }
        return total;
    }

    private int expand(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            ++count;
            --left;
            ++right;
        }
        return count;
    }
}
