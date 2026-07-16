// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class ValidWordAbbr {
    private final Map<String, Set<String>> groups = new HashMap<>();

    public ValidWordAbbr(String[] dictionary) {
        for (String word : dictionary) {
            String key = abbreviate(word);
            groups.computeIfAbsent(key, ignored -> new HashSet<>()).add(word);
        }
    }

    public boolean isUnique(String word) {
        String key = abbreviate(word);
        Set<String> words = groups.getOrDefault(key, Set.of());
        return words.isEmpty() || (words.size() == 1 && words.contains(word));
    }

    private static String abbreviate(String word) {
        if (word.length() <= 2) {
            return word;
        }
        return word.charAt(0) + String.valueOf(word.length() - 2) + word.charAt(word.length() - 1);
    }
}
