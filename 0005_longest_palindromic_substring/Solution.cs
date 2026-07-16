// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

public class Solution {
    public string LongestPalindrome(string s) {
        int bestStart = 0;
        int bestLen = 0;

        for (int i = 0; i < s.Length; i++) {
            int len1 = Expand(s, i, i);
            int len2 = Expand(s, i, i + 1);
            int len = Math.Max(len1, len2);
            if (len > bestLen) {
                bestLen = len;
                bestStart = i - (len - 1) / 2;
            }
        }

        return s.Substring(bestStart, bestLen);
    }

    private static int Expand(string s, int left, int right) {
        while (left >= 0 && right < s.Length && s[left] == s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
