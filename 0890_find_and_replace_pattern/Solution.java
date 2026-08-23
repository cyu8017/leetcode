// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

import java.util.*;

class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        int[] target = normalize(pattern);
        List<String> ans = new ArrayList<>();
        for (String w : words) {
            if (Arrays.equals(normalize(w), target)) ans.add(w);
        }
        return ans;
    }

    private int[] normalize(String s) {
        Map<Character, Integer> mapping = new HashMap<>();
        int[] out = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            mapping.putIfAbsent(ch, mapping.size());
            out[i] = mapping.get(ch);
        }
        return out;
    }
}
