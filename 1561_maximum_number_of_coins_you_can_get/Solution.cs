// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

using System;

public class Solution {
    public int MaxCoins(int[] piles) {
        Array.Sort(piles);
        int ans = 0;
        for (int i = piles.Length / 3; i < piles.Length; i += 2) ans += piles[i];
        return ans;
    }
}
