// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class AutocompleteSystem {
    private final Map<String, Integer> counts = new HashMap<>();
    private final StringBuilder current = new StringBuilder();

    public AutocompleteSystem(String[] sentences, int[] times) {
        for (int i = 0; i < sentences.length; ++i) {
            counts.put(sentences[i], counts.getOrDefault(sentences[i], 0) + times[i]);
        }
    }

    public List<String> input(char c) {
        if (c == '#') {
            String sentence = current.toString();
            counts.put(sentence, counts.getOrDefault(sentence, 0) + 1);
            current.setLength(0);
            return new ArrayList<>();
        }
        current.append(c);
        String prefix = current.toString();
        List<String> matches = new ArrayList<>();
        for (String sentence : counts.keySet()) {
            if (sentence.startsWith(prefix)) {
                matches.add(sentence);
            }
        }
        matches.sort((a, b) -> {
            int ca = counts.get(a);
            int cb = counts.get(b);
            if (ca != cb) {
                return Integer.compare(cb, ca);
            }
            return a.compareTo(b);
        });
        if (matches.size() > 3) {
            return matches.subList(0, 3);
        }
        return matches;
    }
}
