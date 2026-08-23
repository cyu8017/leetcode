// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

import java.util.*;

class Solution {
    public String longestWord(String[] words) {
        Arrays.sort(words);
        Set<String> built = new HashSet<>();
        built.add("");
        String best = "";
        for (String word : words) {
            if (built.contains(word.substring(0, word.length() - 1))) {
                built.add(word);
                if (word.length() > best.length()) best = word;
            }
        }
        return best;
    }
}
