// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public String longestWord(String[] words) {
        Set<String> wordSet = new HashSet<>();
        for (String word : words) {
            wordSet.add(word);
        }

        String best = "";

        for (String word : words) {
            String prefix = word;
            boolean valid = true;
            while (!prefix.isEmpty()) {
                if (!wordSet.contains(prefix)) {
                    valid = false;
                    break;
                }
                prefix = prefix.substring(0, prefix.length() - 1);
            }

            if (valid && (word.length() > best.length()
                    || (word.length() == best.length() && word.compareTo(best) < 0))) {
                best = word;
            }
        }

        return best;
    }
}
