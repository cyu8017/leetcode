// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
    public int appendCharacters(String s, String t) {
        int j = 0;
        for (int i = 0; i < s.length() && j < t.length(); i++) {
            if (s.charAt(i) == t.charAt(j)) j++;
        }
        return t.length() - j;
    }
}
