// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (words.length == 0 || s.isEmpty()) {
            return result;
        }

        int wordLen = words[0].length();
        int wordCount = words.length;
        Map<String, Integer> need = new HashMap<>();
        for (String word : words) {
            need.put(word, need.getOrDefault(word, 0) + 1);
        }

        for (int start = 0; start < wordLen; start++) {
            int left = start;
            Map<String, Integer> counts = new HashMap<>();
            int used = 0;

            for (int right = start; right <= s.length() - wordLen; right += wordLen) {
                String word = s.substring(right, right + wordLen);
                if (!need.containsKey(word)) {
                    counts.clear();
                    used = 0;
                    left = right + wordLen;
                    continue;
                }

                counts.put(word, counts.getOrDefault(word, 0) + 1);
                used++;
                while (counts.get(word) > need.get(word)) {
                    String leftWord = s.substring(left, left + wordLen);
                    counts.put(leftWord, counts.get(leftWord) - 1);
                    used--;
                    left += wordLen;
                }

                if (used == wordCount) {
                    result.add(left);
                }
            }
        }

        result.sort(Integer::compareTo);
        return result;
    }
}
