// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

using System;

public class Solution {
    public long MinimumMoney(int[][] transactions) {
        long totalLoss = 0, maxCashback = 0, maxCost = 0;
        foreach (var t in transactions) {
            long cost = t[0], cashback = t[1];
            if (cost > cashback) {
                totalLoss += cost - cashback;
                maxCashback = Math.Max(maxCashback, cashback);
            } else {
                maxCost = Math.Max(maxCost, cost);
            }
        }
        return Math.Max(totalLoss + maxCashback, totalLoss + maxCost);
    }
}
