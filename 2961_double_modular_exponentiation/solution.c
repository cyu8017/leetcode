// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

#include <stdlib.h>

static int modPow2961(int a, int b, int mod) {
    int res = 1 % mod;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getGoodIndices(int** variables, int variablesSize, int* variablesColSize, int target, int* returnSize) {
    (void)variablesColSize;
    int* ans = (int*)malloc((size_t)variablesSize * sizeof(int));
    int sz = 0;
    for (int i = 0; i < variablesSize; i++) {
        int a = variables[i][0], b = variables[i][1], c = variables[i][2], m = variables[i][3];
        if (modPow2961(modPow2961(a, b, 10), c, m) == target) {
            ans[sz++] = i;
        }
    }
    *returnSize = sz;
    return ans;
}
