// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

#include <stdlib.h>
#include <string.h>

static int cmp3186(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

enum { H3186 = 200003 };
typedef struct { int key, val, used; } E3186;
static E3186 ht3186[H3186];
static int *pwr3186, *nxt3186, n3186;
static long long *memo3186;

static int* cnt3186(int key) {
    unsigned h = ((unsigned)key * 2654435761u) % H3186;
    for (;;) {
        if (!ht3186[h].used) { ht3186[h].used = 1; ht3186[h].key = key; ht3186[h].val = 0; return &ht3186[h].val; }
        if (ht3186[h].key == key) return &ht3186[h].val;
        h = (h + 1) % H3186;
    }
}
static int lb3186(int x) {
    int lo = 0, hi = n3186;
    while (lo < hi) { int mid = (lo + hi) / 2; if (pwr3186[mid] < x) lo = mid + 1; else hi = mid; }
    return lo;
}
static long long dfs3186(int i) {
    if (i >= n3186) return 0;
    if (memo3186[i] != -1) return memo3186[i];
    int c = *cnt3186(pwr3186[i]);
    long long a = dfs3186(i + c);
    long long b = (long long)pwr3186[i] * c + dfs3186(nxt3186[i]);
    return memo3186[i] = a > b ? a : b;
}

long long maximumTotalDamage(int* power, int powerSize) {
    qsort(power, powerSize, sizeof(int), cmp3186);
    pwr3186 = power; n3186 = powerSize;
    memset(ht3186, 0, sizeof(ht3186));
    nxt3186 = malloc(n3186 * sizeof(int));
    memo3186 = malloc(n3186 * sizeof(long long));
    for (int i = 0; i < n3186; i++) {
        (*cnt3186(power[i]))++;
        nxt3186[i] = lb3186(power[i] + 3);
        memo3186[i] = -1;
    }
    long long ans = dfs3186(0);
    free(nxt3186); free(memo3186);
    return ans;
}
