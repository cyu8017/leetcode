// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minimumCardPickup(int[] cards) {
        Map<Integer, Integer> last = new HashMap<>();
        int ans = -1;
        for (int i = 0; i < cards.length; i++) {
            if (last.containsKey(cards[i])) {
                int diff = i - last.get(cards[i]) + 1;
                if (ans == -1 || diff < ans) ans = diff;
            }
            last.put(cards[i], i);
        }
        return ans;
    }
}
