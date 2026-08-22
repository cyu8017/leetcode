// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

#include <stdlib.h>

enum { M3145 = 50 };
static long long cnt3145[M3145 + 1], s3145[M3145 + 1];
static int inited3145 = 0;

static void init3145(void) {
    if (inited3145) return;
    inited3145 = 1;
    long long p = 1;
    cnt3145[0] = 0; s3145[0] = 0;
    for (int i = 1; i <= M3145; i++) {
        cnt3145[i] = cnt3145[i - 1] * 2 + p;
        s3145[i] = s3145[i - 1] * 2 + p * (i - 1);
        p *= 2;
    }
}

static void numIdxAndSum(long long x, long long* idx, long long* totalSum) {
    *idx = 0; *totalSum = 0;
    while (x > 0) {
        int i = 63 - __builtin_clzll((unsigned long long)x);
        *idx += cnt3145[i];
        *totalSum += s3145[i];
        x -= 1LL << i;
        *totalSum += (x + 1) * i;
        *idx += x + 1;
    }
}

static long long f3145(long long i) {
    long long l = 0, r = 1LL << M3145;
    while (l < r) {
        long long mid = (l + r + 1) >> 1;
        long long idx, ts;
        numIdxAndSum(mid, &idx, &ts);
        if (idx < i) l = mid; else r = mid - 1;
    }
    long long totalSum, idx;
    numIdxAndSum(l, &idx, &totalSum);
    i -= idx;
    long long x = l + 1;
    for (long long j = 0; j < i; j++) {
        long long y = x & -x;
        totalSum += __builtin_ctzll((unsigned long long)y);
        x -= y;
    }
    return totalSum;
}

static long long qpow3145(long long a, long long n, long long mod) {
    long long ans = 1 % mod;
    a %= mod;
    while (n > 0) {
        if (n & 1) ans = ans * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return ans;
}

int* findProductsOfElements(long long** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    init3145();
    int* ans = malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        long long left = queries[i][0], right = queries[i][1], mod = queries[i][2];
        long long power = f3145(right + 1) - f3145(left);
        ans[i] = (int)qpow3145(2, power, mod);
    }
    *returnSize = queriesSize;
    return ans;
}
