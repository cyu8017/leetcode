// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution {
    public int removePalindromeSub(String s) {
        if (s.length == 0) return 0;
        int l = 0, r = s.length - 1;
        while (l < r) {
            if (s[l++] != s[r--]) return 2;
        }
        return 1;
    }
}
