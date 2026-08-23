// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

using System.Collections.Generic;

public class Solution {
    public int MinimumCardPickup(int[] cards) {
        var last = new Dictionary<int, int>();
        int ans = -1;
        for (int i = 0; i < cards.Length; i++) {
            if (last.TryGetValue(cards[i], out int prev)) {
                int diff = i - prev + 1;
                if (ans == -1 || diff < ans) ans = diff;
            }
            last[cards[i]] = i;
        }
        return ans;
    }
}
