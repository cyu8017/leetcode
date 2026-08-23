// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution {
    public String largestMerge(String word1, String word2) {
        int i = 0;
        int j = 0;
        StringBuilder out = new StringBuilder();
        while (i < word1.length() && j < word2.length()) {
            if (word1.substring(i).compareTo(word2.substring(j)) > 0) {
                out.append(word1.charAt(i));
                i++;
            } else {
                out.append(word2.charAt(j));
                j++;
            }
        }
        out.append(word1, i, word1.length());
        out.append(word2, j, word2.length());
        return out.toString();
    }
}
