// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    int balance;
} BalanceEntry;

static int dfs(int* debts, int size, int index) {
    while (index < size && debts[index] == 0) {
        index++;
    }
    if (index == size) {
        return 0;
    }
    int best = size;
    for (int nextIndex = index + 1; nextIndex < size; nextIndex++) {
        if ((long long)debts[index] * debts[nextIndex] < 0) {
            debts[nextIndex] += debts[index];
            int candidate = 1 + dfs(debts, size, index + 1);
            if (candidate < best) {
                best = candidate;
            }
            debts[nextIndex] -= debts[index];
        }
    }
    return best;
}

int minTransfers(int** transactions, int transactionsSize, int* transactionsColSize) {
    (void)transactionsColSize;
    BalanceEntry entries[40];
    int entryCount = 0;

    for (int i = 0; i < transactionsSize; i++) {
        int source = transactions[i][0];
        int target = transactions[i][1];
        int amount = transactions[i][2];
        int foundSource = 0;
        int foundTarget = 0;
        for (int j = 0; j < entryCount; j++) {
            if (entries[j].id == source) {
                entries[j].balance -= amount;
                foundSource = 1;
            }
            if (entries[j].id == target) {
                entries[j].balance += amount;
                foundTarget = 1;
            }
        }
        if (!foundSource) {
            entries[entryCount].id = source;
            entries[entryCount].balance = -amount;
            entryCount++;
        }
        if (!foundTarget) {
            entries[entryCount].id = target;
            entries[entryCount].balance = amount;
            entryCount++;
        }
    }

    int debts[40];
    int debtCount = 0;
    for (int i = 0; i < entryCount; i++) {
        if (entries[i].balance != 0) {
            debts[debtCount++] = entries[i].balance;
        }
    }
    return dfs(debts, debtCount, 0);
}
