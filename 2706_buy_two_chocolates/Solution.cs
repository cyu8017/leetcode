// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

using System;

public class Solution {
    public int BuyChoco(int[] prices, int money) {
        Array.Sort(prices);
        int cost = prices[0] + prices[1];
        return cost <= money ? money - cost : money;
    }
}
