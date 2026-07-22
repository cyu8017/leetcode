// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    int best = 0;
    for (int i = 0; i < accountsSize; i++) {
        int s = 0;
        for (int j = 0; j < accountsColSize[i]; j++) s += accounts[i][j];
        if (s > best) best = s;
    }
    return best;
}
