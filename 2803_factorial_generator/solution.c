// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

#include <stdlib.h>

int* factorialGenerator(int n, int* returnSize) {
    int* ans = (int*)malloc((n > 0 ? n : 1) * sizeof(int));
    int cur = 1, sz = 0;
    for (int i = 1; i <= n; i++) {
        cur *= i;
        ans[sz++] = cur;
    }
    *returnSize = sz;
    return ans;
}
