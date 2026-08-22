// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

#include <stdlib.h>

int* missingRolls(int* rolls, int rollsSize, int mean, int n, int* returnSize) {
    int sum = 0;
    for (int i = 0; i < rollsSize; i++) sum += rolls[i];
    int remain = mean * (rollsSize + n) - sum;
    if (remain < n || remain > 6 * n) {
        *returnSize = 0;
        return NULL;
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int base = remain / n, extra = remain % n;
    for (int i = 0; i < n; i++) {
        ans[i] = base;
        if (i < extra) ans[i]++;
    }
    *returnSize = n;
    return ans;
}
