// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

public class Solution {
    public string TrimTrailingVowels(string s) {
        int i = s.Length - 1;
        bool IsVowel(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        while (i >= 0 && IsVowel(s[i])) i--;
        return s.Substring(0, i + 1);
    }
}
