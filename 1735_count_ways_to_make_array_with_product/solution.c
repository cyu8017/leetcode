// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

#include <stdlib.h>

#define MOD 1000000007LL

static long long powMod(long long base, long long exp) {
    long long result = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    return result;
}

static long long combMod(long long a, long long b) {
    long long num = 1;
    long long den = 1;
    for (long long i = 1; i <= b; i++) {
        num = num * ((a - b + i) % MOD) % MOD;
        den = den * (i % MOD) % MOD;
    }
    return num * powMod(den, MOD - 2) % MOD;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* waysToFillArray(int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        long long n = queries[i][0];
        long long value = queries[i][1];
        long long ways = 1;
        long long d = 2;
        while (d * d <= value) {
            if (value % d == 0) {
                long long exp = 0;
                while (value % d == 0) {
                    value /= d;
                    exp++;
                }
                ways = ways * combMod(n + exp - 1, exp) % MOD;
            }
            d += d == 2 ? 1 : 2;
        }
        if (value > 1) {
            ways = ways * (n % MOD) % MOD;
        }
        ans[i] = (int)ways;
    }
    *returnSize = queriesSize;
    return ans;
}
