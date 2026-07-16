// LeetCode 0395 - Longest Substring with At Least K Repeating Characters

// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/



import java.util.HashMap;

import java.util.Map;



class Solution {

    public int longestSubstring(String s, int k) {

        if (s.isEmpty()) {

            return 0;

        }



        Map<Character, Integer> counts = new HashMap<>();

        for (int index = 0; index < s.length(); index++) {

            char character = s.charAt(index);

            counts.put(character, counts.getOrDefault(character, 0) + 1);

        }



        for (Map.Entry<Character, Integer> entry : counts.entrySet()) {

            if (entry.getValue() < k) {

                int best = 0;

                String[] parts = s.split(String.valueOf(entry.getKey()), -1);

                for (String part : parts) {

                    best = Math.max(best, longestSubstring(part, k));

                }

                return best;

            }

        }



        return s.length();

    }

}
