// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

long long minimumMoney(int** transactions, int transactionsSize, int* transactionsColSize) {
    (void)transactionsColSize;
    long long totalLoss = 0, maxCashback = 0, maxCost = 0;
    for (int i = 0; i < transactionsSize; i++) {
        long long cost = transactions[i][0], cashback = transactions[i][1];
        if (cost > cashback) {
            totalLoss += cost - cashback;
            if (cashback > maxCashback) maxCashback = cashback;
        } else if (cost > maxCost) maxCost = cost;
    }
    long long a = totalLoss + maxCashback, b = totalLoss + maxCost;
    return a > b ? a : b;
}
