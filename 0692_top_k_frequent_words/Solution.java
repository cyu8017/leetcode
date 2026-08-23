// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

import java.util.*;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counts = new HashMap<>();
        for (String word : words) counts.put(word, counts.getOrDefault(word, 0) + 1);
        List<String> ordered = new ArrayList<>(counts.keySet());
        ordered.sort((a, b) -> {
            int ca = counts.get(a), cb = counts.get(b);
            if (ca != cb) return Integer.compare(cb, ca);
            return a.compareTo(b);
        });
        return ordered.subList(0, k);
    }
}
