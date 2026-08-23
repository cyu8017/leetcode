// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

import java.util.*;

class Solution {
    private final Map<String, String> parent = new HashMap<>();

    public boolean areSentencesSimilarTwo(String[] sentence1, String[] sentence2, List<List<String>> similarPairs) {
        if (sentence1.length != sentence2.length) return false;
        parent.clear();
        for (List<String> pair : similarPairs) unite(pair.get(0), pair.get(1));
        for (int i = 0; i < sentence1.length; i++) {
            if (!find(sentence1[i]).equals(find(sentence2[i]))) return false;
        }
        return true;
    }

    private String find(String x) {
        parent.putIfAbsent(x, x);
        while (!parent.get(x).equals(x)) {
            parent.put(x, parent.get(parent.get(x)));
            x = parent.get(x);
        }
        return x;
    }

    private void unite(String a, String b) {
        parent.put(find(a), find(b));
    }
}
