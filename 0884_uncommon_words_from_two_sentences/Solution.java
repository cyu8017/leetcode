// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

import java.util.*;

class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        Map<String, Integer> count = new HashMap<>();
        add(count, s1);
        add(count, s2);
        List<String> ans = new ArrayList<>();
        for (Map.Entry<String, Integer> kv : count.entrySet()) {
            if (kv.getValue() == 1) ans.add(kv.getKey());
        }
        return ans.toArray(new String[0]);
    }

    private void add(Map<String, Integer> count, String s) {
        for (String w : s.split(" ")) {
            if (w.isEmpty()) continue;
            count.put(w, count.getOrDefault(w, 0) + 1);
        }
    }
}
