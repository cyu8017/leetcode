// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

export function minimumMoney(transactions: number[][]): number {
    let totalLoss = 0, maxCashback = 0, maxCost = 0;
    for (const t of transactions) {
        const cost = t[0], cashback = t[1];
        if (cost > cashback) {
            totalLoss += cost - cashback;
            maxCashback = Math.max(maxCashback, cashback);
        } else {
            maxCost = Math.max(maxCost, cost);
        }
    }
    return Math.max(totalLoss + maxCashback, totalLoss + maxCost);
}
