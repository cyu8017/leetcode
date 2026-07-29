// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

#include <stdlib.h>
#include <stdint.h>

typedef struct { uint64_t a, b; } Hash;

static int cmpHash(const void* x, const void* y) {
    const Hash* p = x; const Hash* q = y;
    if (p->a < q->a) return -1;
    if (p->a > q->a) return 1;
    if (p->b < q->b) return -1;
    if (p->b > q->b) return 1;
    return 0;
}

static int hasCommon(int length, int** paths, int pathsSize, int* pathsColSize) {
    if (length == 0) return 1;
    const uint64_t BASE1 = 911382323ULL, MOD1 = 1000000007ULL;
    const uint64_t BASE2 = 972663749ULL, MOD2 = 1000000009ULL;
    Hash* common = NULL;
    int commonN = 0;
    int first = 1;
    for (int p = 0; p < pathsSize; p++) {
        if (pathsColSize[p] < length) { free(common); return 0; }
        uint64_t pow1 = 1, pow2 = 1;
        for (int i = 0; i < length; i++) {
            pow1 = pow1 * BASE1 % MOD1;
            pow2 = pow2 * BASE2 % MOD2;
        }
        Hash* seen = (Hash*)malloc((size_t)(pathsColSize[p] - length + 1) * sizeof(Hash));
        int sn = 0;
        uint64_t h1 = 0, h2 = 0;
        for (int i = 0; i < pathsColSize[p]; i++) {
            h1 = (h1 * BASE1 + (uint64_t)paths[p][i] + 1) % MOD1;
            h2 = (h2 * BASE2 + (uint64_t)paths[p][i] + 1) % MOD2;
            if (i >= length) {
                h1 = (h1 + MOD1 - ((uint64_t)paths[p][i - length] + 1) * pow1 % MOD1) % MOD1;
                h2 = (h2 + MOD2 - ((uint64_t)paths[p][i - length] + 1) * pow2 % MOD2) % MOD2;
            }
            if (i >= length - 1) {
                seen[sn].a = h1;
                seen[sn].b = h2;
                sn++;
            }
        }
        qsort(seen, (size_t)sn, sizeof(Hash), cmpHash);
        int uniq = 0;
        for (int i = 0; i < sn; i++) {
            if (i == 0 || cmpHash(&seen[i], &seen[i - 1]) != 0) seen[uniq++] = seen[i];
        }
        sn = uniq;
        if (first) {
            common = seen;
            commonN = sn;
            first = 0;
        } else {
            Hash* nxt = (Hash*)malloc((size_t)commonN * sizeof(Hash));
            int nn = 0;
            int i = 0, j = 0;
            while (i < commonN && j < sn) {
                int c = cmpHash(&common[i], &seen[j]);
                if (c == 0) { nxt[nn++] = common[i]; i++; j++; }
                else if (c < 0) i++;
                else j++;
            }
            free(common);
            free(seen);
            common = nxt;
            commonN = nn;
            if (!commonN) { free(common); return 0; }
        }
    }
    free(common);
    return 1;
}

int longestCommonSubpath(int n, int** paths, int pathsSize, int* pathsColSize) {
    (void)n;
    int lo = 0, hi = pathsColSize[0];
    for (int i = 1; i < pathsSize; i++) if (pathsColSize[i] < hi) hi = pathsColSize[i];
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (hasCommon(mid, paths, pathsSize, pathsColSize)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
