// LeetCode 1328 - Break A Palindrome
// https://leetcode.com/problems/break-a-palindrome/

public class Solution {
    public string BreakPalindrome(string palindrome) {
        if (palindrome.Length == 1) return "";
        char[] chars = palindrome.ToCharArray();
        for (int i = 0; i < chars.Length / 2; i++) {
            if (chars[i] != 'a') {
                chars[i] = 'a';
                return new string(chars);
            }
        }
        chars[chars.Length - 1] = 'b';
        return new string(chars);
    }
}
