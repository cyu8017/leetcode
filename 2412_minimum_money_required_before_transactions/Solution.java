// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

class Solution {
    public long minimumMoney(int[][] transactions) {
        long totalLoss = 0, maxCashback = 0, maxCost = 0;
        for (int[] t : transactions) {
            long cost = t[0], cashback = t[1];
            if (cost > cashback) {
                totalLoss += cost - cashback;
                maxCashback = Math.max(maxCashback, cashback);
            } else {
                maxCost = Math.max(maxCost, cost);
            }
        }
        return Math.max(totalLoss + maxCashback, totalLoss + maxCost);
    }
}
