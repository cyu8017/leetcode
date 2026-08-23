// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) {
            return "";
        }

        Map<Character, Integer> need = new HashMap<>();
        for (char ch : t.toCharArray()) {
            need.put(ch, need.getOrDefault(ch, 0) + 1);
        }

        int required = need.size();
        int formed = 0;
        Map<Character, Integer> window = new HashMap<>();
        int left = 0;
        int bestLen = Integer.MAX_VALUE;
        int bestLeft = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            window.put(ch, window.getOrDefault(ch, 0) + 1);
            if (need.containsKey(ch) && window.get(ch).equals(need.get(ch))) {
                formed++;
            }

            while (formed == required) {
                if (right - left + 1 < bestLen) {
                    bestLen = right - left + 1;
                    bestLeft = left;
                }

                char leftCh = s.charAt(left);
                window.put(leftCh, window.get(leftCh) - 1);
                if (need.containsKey(leftCh) && window.get(leftCh) < need.get(leftCh)) {
                    formed--;
                }
                left++;
            }
        }

        if (bestLen == Integer.MAX_VALUE) {
            return "";
        }

        return s.substring(bestLeft, bestLeft + bestLen);
    }
}
