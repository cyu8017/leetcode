// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

class Solution {
    public String longestPrefix(String s) {
        if (s.length == 0) return "";
        var pi = new int[s.length];
        for (int i = 1; i < s.length; i++) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) j = pi[j - 1];
            if (s[i] == s[j]) j++;
            pi[i] = j;
        }
        return s.SubString(0, pi[s.length - 1]);
    }
}
