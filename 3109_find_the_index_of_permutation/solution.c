// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

#include <stdlib.h>

typedef struct { int n; int* c; } BIT;
static BIT* bit_new(int n) {
    BIT* b = (BIT*)malloc(sizeof(BIT));
    b->n = n; b->c = (int*)calloc((size_t)(n + 1), sizeof(int));
    return b;
}
static void bit_upd(BIT* b, int x, int d) { for (; x <= b->n; x += x & -x) b->c[x] += d; }
static int bit_qry(BIT* b, int x) { int s = 0; for (; x > 0; x -= x & -x) s += b->c[x]; return s; }

int getPermutationIndex(int* perm, int permSize) {
    const int mod = 1000000007;
    int n = permSize;
    BIT* tree = bit_new(n + 1);
    int* f = (int*)malloc((size_t)n * sizeof(int));
    f[0] = 1;
    for (int i = 1; i < n; i++) f[i] = (int)((1LL * f[i - 1] * i) % mod);
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int x = perm[i];
        int cnt = x - 1 - bit_qry(tree, x);
        ans = (ans + 1LL * cnt * f[n - 1 - i]) % mod;
        bit_upd(tree, x, 1);
    }
    free(f); free(tree->c); free(tree);
    return (int)ans;
}
