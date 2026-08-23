// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

public class Solution {
    public int AppendCharacters(string s, string t) {
        int j = 0;
        for (int i = 0; i < s.Length && j < t.Length; i++) {
            if (s[i] == t[j]) j++;
        }
        return t.Length - j;
    }
}
