// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

#include <stdlib.h>
#include <string.h>

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

#define MAP_SIZE 10007
typedef struct { int k, v; char u; } Slot;
static Slot dp[MAP_SIZE], ndp[MAP_SIZE];

static void clear(Slot* m) { for (int i = 0; i < MAP_SIZE; i++) m[i].u = 0; }
static int* get(Slot* m, int k) {
    unsigned i = (unsigned)k % MAP_SIZE;
    for (;;) {
        if (!m[i].u) { m[i].u = 1; m[i].k = k; m[i].v = 0; return &m[i].v; }
        if (m[i].k == k) return &m[i].v;
        if (++i == MAP_SIZE) i = 0;
    }
}
static int has(Slot* m, int k, int* out) {
    unsigned i = (unsigned)k % MAP_SIZE;
    for (;;) {
        if (!m[i].u) return 0;
        if (m[i].k == k) { *out = m[i].v; return 1; }
        if (++i == MAP_SIZE) i = 0;
    }
}

int countCoprime(int** mat, int matSize, int* matColSize) {
    const int MOD = 1000000007;
    clear(dp);
    for (int j = 0; j < matColSize[0]; j++) {
        (*get(dp, mat[0][j]))++;
    }
    for (int i = 1; i < matSize; i++) {
        clear(ndp);
        for (int j = 0; j < matColSize[i]; j++) {
            int v = mat[i][j];
            for (int t = 0; t < MAP_SIZE; t++) {
                if (!dp[t].u) continue;
                int ng = gcd(dp[t].k, v);
                int* p = get(ndp, ng);
                *p = (*p + dp[t].v) % MOD;
            }
        }
        memcpy(dp, ndp, sizeof(dp));
    }
    int ans = 0;
    has(dp, 1, &ans);
    return ans;
}
