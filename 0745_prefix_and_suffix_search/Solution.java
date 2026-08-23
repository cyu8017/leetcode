// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

import java.util.*;

class WordFilter {
    private final Map<String, Integer> lookup = new HashMap<>();

    public WordFilter(String[] words) {
        for (int index = 0; index < words.length; index++) {
            String word = words[index];
            int size = word.length();
            for (int i = 0; i <= size; i++) {
                for (int j = 0; j <= size; j++) {
                    lookup.put(word.substring(0, i) + "#" + word.substring(j), index);
                }
            }
        }
    }

    public int f(String pref, String suff) {
        return lookup.getOrDefault(pref + "#" + suff, -1);
    }
}
