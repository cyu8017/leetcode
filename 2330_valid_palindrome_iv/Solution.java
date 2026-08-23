// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

class Solution {
    public boolean makePalindrome(String s) {
        int diff = 0;
        for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
            if (s.charAt(i) != s.charAt(j)) {
                diff++;
                if (diff > 2) return false;
            }
        }
        return true;
    }
}
