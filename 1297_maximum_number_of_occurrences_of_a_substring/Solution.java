// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

import java.util.*;

class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        HashMap<String, Integer> counts = new HashMap<>();
        for (int i = 0; i + minSize <= s.length(); i++) {
            String sub = s.substring(i, i + minSize);
            HashSet<Character> seen = new HashSet<>();
            for (char ch : sub.toCharArray()) seen.add(ch);
            if (seen.size() <= maxLetters) {
                counts.put(sub, counts.getOrDefault(sub, 0) + 1);
            }
        }
        int best = 0;
        for (int freq : counts.values()) best = Math.max(best, freq);
        return best;
    }
}
