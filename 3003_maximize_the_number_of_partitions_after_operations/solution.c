// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int popcount(unsigned x) { int c=0; while(x){c+=x&1;x>>=1;} return c; }
static int imax(int a, int b) { return a > b ? a : b; }

typedef struct { long long key; int val; bool used; } HEnt;
static unsigned hash_ll(unsigned long long x) {
    x ^= x >> 30; x *= 0xbf58476d1ce4e5b9ULL; x ^= x >> 27; x *= 0x94d049bb133111ebULL; x ^= x >> 31;
    return (unsigned)x;
}
static bool hget(HEnt* t, int cap, long long key, int* out) {
    unsigned h = hash_ll((unsigned long long)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { *out = t[h].val; return true; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    return false;
}
static void hset(HEnt* t, int cap, long long key, int val) {
    unsigned h = hash_ll((unsigned long long)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val = val; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = val;
}

static const char* s3003;
static int n3003, k3003, cap3003;
static HEnt* memo3003;

static int dfs3003(int i, int cur, int t) {
    if (i >= n3003) return 1;
    long long key = ((long long)i << 32) | ((long long)cur << 1) | t;
    int cached;
    if (hget(memo3003, cap3003, key, &cached)) return cached;
    int v = 1 << (s3003[i] - 'a');
    int nxt = cur | v;
    int ans;
    if (popcount((unsigned)nxt) > k3003) ans = dfs3003(i + 1, v, t) + 1;
    else ans = dfs3003(i + 1, nxt, t);
    if (t > 0) {
        for (int j = 0; j < 26; j++) {
            nxt = cur | (1 << j);
            if (popcount((unsigned)nxt) > k3003) ans = imax(ans, dfs3003(i + 1, 1 << j, 0) + 1);
            else ans = imax(ans, dfs3003(i + 1, nxt, 0));
        }
    }
    hset(memo3003, cap3003, key, ans);
    return ans;
}

int maxPartitionsAfterOperations(char* s, int k) {
    s3003 = s; n3003 = (int)strlen(s); k3003 = k;
    cap3003 = 1 << 20;
    memo3003 = (HEnt*)calloc((size_t)cap3003, sizeof(HEnt));
    int ans = dfs3003(0, 0, 1);
    free(memo3003);
    return ans;
}
