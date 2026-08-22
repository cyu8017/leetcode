// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

#include <stdlib.h>

typedef struct { long long key; int cnt; int used; } MapE;

typedef struct { MapE* tab; int cap; } LMap;

static unsigned h64(long long k) { return (unsigned)(k * 2654435761u); }

static LMap* lmapNew(int cap) {
    LMap* m = (LMap*)malloc(sizeof(LMap));
    m->cap = cap;
    m->tab = (MapE*)calloc((size_t)cap, sizeof(MapE));
    return m;
}

static void lmapFree(LMap* m) { free(m->tab); free(m); }

static int* lmapRef(LMap* m, long long key, int create) {
    int idx = (int)(h64(key) & (unsigned)(m->cap - 1));
    for (;;) {
        if (!m->tab[idx].used) {
            if (!create) return NULL;
            m->tab[idx].used = 1;
            m->tab[idx].key = key;
            m->tab[idx].cnt = 0;
            return &m->tab[idx].cnt;
        }
        if (m->tab[idx].key == key) return &m->tab[idx].cnt;
        idx = (idx + 1) & (m->cap - 1);
    }
}

static int lmapGet(LMap* m, long long key) {
    int* p = lmapRef(m, key, 0);
    return p ? *p : 0;
}

int waysToPartition(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long* pref = (long long*)malloc((size_t)n * sizeof(long long));
    pref[0] = nums[0];
    for (int i = 1; i < n; i++) pref[i] = pref[i - 1] + nums[i];
    long long total = pref[n - 1];
    int cap = 1;
    while (cap < n * 4) cap *= 2;
    LMap* right = lmapNew(cap);
    LMap* left = lmapNew(cap);
    for (int i = 0; i < n - 1; i++) (*lmapRef(right, pref[i], 1))++;
    int ans = 0;
    if (total % 2 == 0) ans = lmapGet(right, total / 2);
    for (int i = 0; i < n; i++) {
        long long diff = (long long)k - nums[i];
        long long newTotal = total + diff;
        int cur = 0;
        if (newTotal % 2 == 0) {
            long long half = newTotal / 2;
            cur = lmapGet(left, half) + lmapGet(right, half - diff);
        }
        if (cur > ans) ans = cur;
        if (i < n - 1) {
            (*lmapRef(left, pref[i], 1))++;
            (*lmapRef(right, pref[i], 1))--;
        }
    }
    free(pref); lmapFree(left); lmapFree(right);
    return ans;
}
