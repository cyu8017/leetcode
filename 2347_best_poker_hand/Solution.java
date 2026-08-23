// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String bestHand(int[] ranks, char[] suits) {
        if (suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4])
            return "Flush";
        Map<Integer, Integer> cnt = new HashMap<>();
        int best = 0;
        for (int r : ranks) {
            int c = cnt.getOrDefault(r, 0) + 1;
            cnt.put(r, c);
            best = Math.max(best, c);
        }
        if (best >= 3) return "Three of a Kind";
        if (best == 2) return "Pair";
        return "High Card";
    }
}
