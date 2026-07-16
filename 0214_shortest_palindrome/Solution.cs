// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

public class Solution {
    public string ShortestPalindrome(string s) {
        if (string.IsNullOrEmpty(s)) {
            return "";
        }
        var reversed = new string(s.Reverse().ToArray());
        var combined = s + "#" + reversed;
        var pi = new int[combined.Length];
        var lps = 0;
        for (var i = 1; i < combined.Length; i++) {
            while (lps > 0 && combined[i] != combined[lps]) {
                lps = pi[lps - 1];
            }
            if (combined[i] == combined[lps]) {
                lps++;
            }
            pi[i] = lps;
        }
        var prefixLen = pi[combined.Length - 1];
        return reversed.Substring(0, s.Length - prefixLen) + s;
    }
}
