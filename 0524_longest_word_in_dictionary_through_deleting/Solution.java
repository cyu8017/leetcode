// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

import java.util.List;

class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        String best = "";
        for (String word : dictionary) {
            if (isSubsequence(word, s)
                    && (word.length() > best.length()
                            || (word.length() == best.length() && word.compareTo(best) < 0))) {
                best = word;
            }
        }
        return best;
    }

    private boolean isSubsequence(String word, String source) {
        int index = 0;
        for (int pos = 0; pos < source.length(); pos++) {
            if (index < word.length() && word.charAt(index) == source.charAt(pos)) {
                index++;
            }
        }
        return index == word.length();
    }
}
