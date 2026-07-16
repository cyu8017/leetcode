// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (char ch : s.toCharArray()) {
            counts.merge(ch, 1, Integer::sum);
        }
        List<Map.Entry<Character, Integer>> ordered = new ArrayList<>(counts.entrySet());
        ordered.sort((a, b) -> {
            if (!a.getValue().equals(b.getValue())) {
                return Integer.compare(b.getValue(), a.getValue());
            }
            return Character.compare(a.getKey(), b.getKey());
        });
        StringBuilder result = new StringBuilder();
        for (Map.Entry<Character, Integer> entry : ordered) {
            result.append(String.valueOf(entry.getKey()).repeat(entry.getValue()));
        }
        return result.toString();
    }
}
