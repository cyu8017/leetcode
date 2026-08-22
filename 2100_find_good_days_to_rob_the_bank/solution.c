// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

#include <stdlib.h>

int* goodDaysToRobBank(int* security, int securitySize, int time, int* returnSize) {
    int n = securitySize;
    if (time == 0) {
        int* ans = (int*)malloc((size_t)n * sizeof(int));
        for (int i = 0; i < n; i++) ans[i] = i;
        *returnSize = n;
        return ans;
    }
    int* left = (int*)calloc((size_t)n, sizeof(int));
    int* right = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) if (security[i] <= security[i - 1]) left[i] = left[i - 1] + 1;
    for (int i = n - 2; i >= 0; i--) if (security[i] <= security[i + 1]) right[i] = right[i + 1] + 1;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int an = 0;
    for (int i = time; i < n - time; i++) if (left[i] >= time && right[i] >= time) ans[an++] = i;
    free(left); free(right);
    *returnSize = an;
    return ans;
}
