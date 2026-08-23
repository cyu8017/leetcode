// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        Set<String> roots = new HashSet<>(dictionary);
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();
        for (int w = 0; w < words.length; ++w) {
            String word = words[w];
            String replacement = word;
            for (int i = 1; i <= word.length(); ++i) {
                String prefix = word.substring(0, i);
                if (roots.contains(prefix)) {
                    replacement = prefix;
                    break;
                }
            }
            if (w > 0) {
                result.append(' ');
            }
            result.append(replacement);
        }
        return result.toString();
    }
}
