// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

using System;

public class Solution {
    public int TimeRequiredToBuy(int[] tickets, int k) {
        int ans = 0;
        for (int i = 0; i < tickets.Length; i++) {
            if (i <= k) ans += Math.Min(tickets[i], tickets[k]);
            else ans += Math.Min(tickets[i], tickets[k] - 1);
        }
        return ans;
    }
}
