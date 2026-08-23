// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> counts = new HashMap<>();
        int left = 0;
        int best = 0;
        int maxCount = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            counts.put(ch, counts.getOrDefault(ch, 0) + 1);
            maxCount = Math.max(maxCount, counts.get(ch));
            while ((right - left + 1) - maxCount > k) {
                char leftChar = s.charAt(left);
                counts.put(leftChar, counts.get(leftChar) - 1);
                left++;
            }
            best = Math.max(best, right - left + 1);
        }

        return best;
    }
}
