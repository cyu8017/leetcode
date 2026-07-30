// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

public class Solution {
    public string LongestPrefix(string s) {
        if (s.Length == 0) return "";
        var pi = new int[s.Length];
        for (int i = 1; i < s.Length; i++) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) j = pi[j - 1];
            if (s[i] == s[j]) j++;
            pi[i] = j;
        }
        return s.Substring(0, pi[s.Length - 1]);
    }
}
