// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

char** invalidTransactions(char** transactions, int transactionsSize, int* returnSize) {
    char names[1005][15], cities[1005][15];
    int times[1005], amounts[1005];
    bool bad[1005] = {false};
    for (int i = 0; i < transactionsSize; i++) {
        sscanf(transactions[i], "%[^,],%d,%d,%s", names[i], &times[i], &amounts[i], cities[i]);
        if (amounts[i] > 1000) bad[i] = true;
    }
    for (int i = 0; i < transactionsSize; i++) {
        for (int j = i + 1; j < transactionsSize; j++) {
            if (strcmp(names[i], names[j]) == 0 && strcmp(cities[i], cities[j]) != 0) {
                int d = times[i] - times[j];
                if (d < 0) d = -d;
                if (d <= 60) { bad[i] = true; bad[j] = true; }
            }
        }
    }
    char** ans = (char**)malloc((size_t)transactionsSize * sizeof(char*));
    int idx = 0;
    for (int i = 0; i < transactionsSize; i++) {
        if (bad[i]) {
            ans[idx] = (char*)malloc(strlen(transactions[i]) + 1);
            strcpy(ans[idx], transactions[i]);
            idx++;
        }
    }
    *returnSize = idx;
    return ans;
}
