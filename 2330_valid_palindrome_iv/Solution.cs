// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

public class Solution {
    public bool MakePalindrome(string s) {
        int diff = 0;
        for (int i = 0, j = s.Length - 1; i < j; ++i, --j) {
            if (s[i] != s[j]) {
                diff++;
                if (diff > 2) return false;
            }
        }
        return true;
    }
}
