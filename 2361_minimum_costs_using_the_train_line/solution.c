// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

#include <stdlib.h>

static long long min64(long long a, long long b) { return a < b ? a : b; }

long long* minimumCosts(int* regular, int regularSize, int* express, int expressSize, int expressCost, int* returnSize) {
    (void)expressSize;
    int n = regularSize;
    long long* ans = (long long*)malloc((size_t)n * sizeof(long long));
    long long reg = 0, exp = expressCost;
    for (int i = 0; i < n; i++) {
        long long nextReg = min64(reg + regular[i], exp + express[i]);
        long long nextExp = min64(reg + regular[i] + expressCost, exp + express[i]);
        reg = nextReg; exp = nextExp;
        ans[i] = min64(reg, exp);
    }
    *returnSize = n;
    return ans;
}
