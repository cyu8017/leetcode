// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

enum { BASE3213 = 13331, MOD3213 = 998244353, INF3213 = INT_MAX / 2, H3213 = 200003 };

typedef struct { long long key; int val; int used; } E3213;

static long long* p3213; static long long* h3213; static int n3213;

static long long query3213(int l, int r) {
    return (h3213[r] - h3213[l - 1] * p3213[r - l + 1] % MOD3213 + MOD3213) % MOD3213;
}

static int* dget(E3213* d, long long key, int create) {
    unsigned idx = (unsigned)(key % H3213);
    for (;;) {
        if (!d[idx].used) {
            if (!create) return NULL;
            d[idx].used = 1; d[idx].key = key; d[idx].val = INF3213;
            return &d[idx].val;
        }
        if (d[idx].key == key) return &d[idx].val;
        idx = (idx + 1) % H3213;
    }
}

static int cmp3213(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minimumCost(char* target, char** words, int wordsSize, int* costs, int costsSize) {
    (void)costsSize;
    n3213 = (int)strlen(target);
    p3213 = malloc((n3213 + 1) * sizeof(long long));
    h3213 = malloc((n3213 + 1) * sizeof(long long));
    p3213[0] = 1; h3213[0] = 0;
    for (int i = 1; i <= n3213; i++) {
        p3213[i] = p3213[i - 1] * BASE3213 % MOD3213;
        h3213[i] = (h3213[i - 1] * BASE3213 + (unsigned char)target[i - 1]) % MOD3213;
    }
    int* f = malloc((n3213 + 1) * sizeof(int));
    for (int i = 0; i <= n3213; i++) f[i] = INF3213;
    f[0] = 0;
    int* lengths = malloc(wordsSize * sizeof(int));
    int ln = 0;
    for (int i = 0; i < wordsSize; i++) {
        int L = (int)strlen(words[i]);
        int found = 0;
        for (int t = 0; t < ln; t++) if (lengths[t] == L) { found = 1; break; }
        if (!found) lengths[ln++] = L;
    }
    qsort(lengths, ln, sizeof(int), cmp3213);
    E3213* d = calloc(H3213, sizeof(E3213));
    for (int i = 0; i < wordsSize; i++) {
        long long x = 0;
        for (char* c = words[i]; *c; c++) x = (x * BASE3213 + (unsigned char)*c) % MOD3213;
        int* pv = dget(d, x, 1);
        if (costs[i] < *pv) *pv = costs[i];
    }
    for (int i = 1; i <= n3213; i++) {
        for (int t = 0; t < ln; t++) {
            int j = lengths[t];
            if (j > i) break;
            long long x = query3213(i - j + 1, i);
            int* pc = dget(d, x, 0);
            if (pc) {
                int v = f[i - j] + *pc;
                if (v < f[i]) f[i] = v;
            }
        }
    }
    int ans = f[n3213] >= INF3213 ? -1 : f[n3213];
    free(p3213); free(h3213); free(f); free(lengths); free(d);
    return ans;
}
