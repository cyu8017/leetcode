// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

using System;
using System.Collections.Generic;

public class Solution {
    public string BestHand(int[] ranks, char[] suits) {
        if (suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4])
            return "Flush";
        var cnt = new Dictionary<int, int>();
        int best = 0;
        foreach (int r in ranks) {
            if (!cnt.ContainsKey(r)) cnt[r] = 0;
            best = Math.Max(best, ++cnt[r]);
        }
        if (best >= 3) return "Three of a Kind";
        if (best == 2) return "Pair";
        return "High Card";
    }
}
