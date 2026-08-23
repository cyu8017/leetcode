// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder out = new StringBuilder();
        int i = 0;
        int j = 0;
        while (i < word1.length() || j < word2.length()) {
            if (i < word1.length()) {
                out.append(word1.charAt(i++));
            }
            if (j < word2.length()) {
                out.append(word2.charAt(j++));
            }
        }
        return out.toString();
    }
}
