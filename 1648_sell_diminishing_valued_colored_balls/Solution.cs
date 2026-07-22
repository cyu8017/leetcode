// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

using System;
using System.Linq;

public class Solution {
    public int MaxProfit(int[] inventory, int orders) {
        const long MOD = 1000000007;
        Array.Sort(inventory);
        Array.Reverse(inventory);
        var inv = inventory.Concat(new[] { 0 }).ToArray();
        long ans = 0;
        for (int i = 0; i + 1 < inv.Length; i++) {
            long width = i + 1;
            long high = inv[i], low = inv[i + 1];
            long balls = width * (high - low);
            long take = Math.Min(orders, balls);
            long full = take / width, rem = take % width;
            long bottom = high - full;
            ans += width * (high + bottom + 1) * full / 2 + rem * bottom;
            orders -= (int)take;
            if (orders == 0) break;
        }
        return (int)(ans % MOD);
    }
}
