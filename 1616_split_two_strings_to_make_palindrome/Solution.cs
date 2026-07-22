// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

public class Solution {
    public bool CheckPalindromeFormation(string a, string b) {
        return Check(a, b) || Check(b, a);
    }

    private static bool Check(string x, string y) {
        int i = 0, j = x.Length - 1;
        while (i < j && x[i] == y[j]) { i++; j--; }
        return IsPalindrome(x, i, j) || IsPalindrome(y, i, j);
    }

    private static bool IsPalindrome(string s, int i, int j) {
        while (i < j) {
            if (s[i++] != s[j--]) return false;
        }
        return true;
    }
}
