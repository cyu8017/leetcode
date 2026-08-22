// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int** findPrimePairs(int n, int* returnSize, int** returnColumnSizes) {
    bool* isPrime = (bool*)calloc(n + 1, sizeof(bool));
    for (int i = 2; i <= n; i++) isPrime[i] = true;
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) isPrime[j] = false;
        }
    }
    int cap = n / 2 + 1;
    int** ans = (int**)malloc(cap * sizeof(int*));
    *returnColumnSizes = (int*)malloc(cap * sizeof(int));
    int sz = 0;
    for (int x = 2; x <= n / 2; x++) {
        int y = n - x;
        if (isPrime[x] && isPrime[y]) {
            ans[sz] = (int*)malloc(2 * sizeof(int));
            ans[sz][0] = x;
            ans[sz][1] = y;
            (*returnColumnSizes)[sz] = 2;
            sz++;
        }
    }
    free(isPrime);
    *returnSize = sz;
    return ans;
}
