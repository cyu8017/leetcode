// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String[] wordsAbbreviation(String[] words) {
        int[] prefixes = new int[words.length];
        for (int index = 0; index < words.length; index++) {
            prefixes[index] = 1;
        }

        boolean changed = true;
        while (changed) {
            changed = false;
            Map<String, List<Integer>> groups = new HashMap<>();
            for (int index = 0; index < words.length; index++) {
                String key = abbreviate(words[index], prefixes[index]);
                groups.computeIfAbsent(key, ignored -> new ArrayList<>()).add(index);
            }
            for (List<Integer> indices : groups.values()) {
                if (indices.size() > 1) {
                    changed = true;
                    for (int index : indices) {
                        prefixes[index]++;
                    }
                }
            }
        }

        String[] result = new String[words.length];
        for (int index = 0; index < words.length; index++) {
            result[index] = abbreviate(words[index], prefixes[index]);
        }
        return result;
    }

    private String abbreviate(String word, int prefix) {
        if (prefix + 2 >= word.length()) {
            return word;
        }
        int middle = word.length() - prefix - 1;
        String candidate = word.substring(0, prefix) + middle + word.charAt(word.length() - 1);
        return candidate.length() < word.length() ? candidate : word;
    }
}
