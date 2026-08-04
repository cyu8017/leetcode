// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

import java.util.*;

class Solution {
    public List<String> generateSentences(List<List<String>> synonyms, String text) {
        Map<String, String> parent = new HashMap<>();
        for (List<String> pair : synonyms) {
            String a = find(pair.get(0), parent), b = find(pair.get(1), parent);
            parent.put(a, b);
        }
        Map<String, List<String>> groups = new HashMap<>();
        for (String word : parent.keySet()) {
            groups.computeIfAbsent(find(word, parent), k -> new ArrayList<>()).add(word);
        }
        for (List<String> g : groups.values()) Collections.sort(g);
        String[] tokens = text.split(" ");
        List<List<String>> choices = new ArrayList<>();
        for (String w : tokens) {
            if (parent.containsKey(w)) choices.add(groups.get(find(w, parent)));
            else choices.add(List.of(w));
        }
        List<String> answer = new ArrayList<>();
        backtrack(choices, 0, new ArrayList<>(), answer);
        return answer;
    }

    private String find(String x, Map<String, String> parent) {
        parent.putIfAbsent(x, x);
        if (!parent.get(x).equals(x)) parent.put(x, find(parent.get(x), parent));
        return parent.get(x);
    }

    private void backtrack(List<List<String>> choices, int idx, List<String> cur, List<String> answer) {
        if (idx == choices.size()) {
            answer.add(String.join(" ", cur));
            return;
        }
        for (String w : choices.get(idx)) {
            cur.add(w);
            backtrack(choices, idx + 1, cur, answer);
            cur.remove(cur.size() - 1);
        }
    }
}

