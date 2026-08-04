// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

import java.util.*;

class Solution {
    public int longestWPI(int[] hours) {
        int score = 0, ans = 0;
        Map<Integer, Integer> firstSeen = new HashMap<>();
        firstSeen.put(0, -1);
        for (int i = 0; i < hours.length; i++) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) ans = i + 1;
            else if (firstSeen.containsKey(score - 1)) {
                ans = Math.max(ans, i - firstSeen.get(score - 1));
            }
            firstSeen.putIfAbsent(score, i);
        }
        return ans;
    }
}
