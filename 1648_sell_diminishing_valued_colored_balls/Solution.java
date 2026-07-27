// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int maxProfit(int[] inventory, int orders) {
        Arrays.sort(inventory);
        for (int i = 0, j = inventory.length - 1; i < j; i++, j--) {
            int tmp = inventory[i];
            inventory[i] = inventory[j];
            inventory[j] = tmp;
        }
        long[] inv = new long[inventory.length + 1];
        for (int i = 0; i < inventory.length; i++) inv[i] = inventory[i];
        inv[inventory.length] = 0;
        long ans = 0;
        long remaining = orders;
        for (int i = 0; i < inv.length - 1 && remaining > 0; i++) {
            long width = i + 1;
            long high = inv[i], low = inv[i + 1];
            long balls = width * (high - low);
            long take = Math.min(remaining, balls);
            long full = take / width;
            long rem = take % width;
            long bottom = high - full;
            ans += width * (high + bottom + 1) * full / 2 + rem * bottom;
            remaining -= take;
        }
        return (int) (ans % MOD);
    }
}
