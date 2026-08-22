// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

#include <stdlib.h>
#include <string.h>

enum { MOD3935 = 1000000007, HS3935 = 200003 };

typedef struct { int key, val, used; } Ent3935;
static Ent3935 L3935[HS3935], R3935[HS3935];
static int sz1_3935, sz2_3935;

static unsigned hash3935(int x) {
    return (unsigned)(x * 2654435761u) % HS3935;
}
static int* getSlot3935(Ent3935* st, int x, int create) {
    unsigned h = hash3935(x);
    for (int i = 0; i < HS3935; i++) {
        unsigned j = (h + i) % HS3935;
        if (!st[j].used) {
            if (!create) return NULL;
            st[j].used = 1; st[j].key = x; st[j].val = 0;
            return &st[j].val;
        }
        if (st[j].key == x) return &st[j].val;
    }
    return NULL;
}
static void merge3935(Ent3935* st, int x, int v) {
    int* c = getSlot3935(st, x, 1);
    *c += v;
    if (*c == 0) {
        /* remove */
        unsigned h = hash3935(x);
        for (int i = 0; i < HS3935; i++) {
            unsigned j = (h + i) % HS3935;
            if (st[j].used && st[j].key == x) { st[j].used = 0; break; }
        }
    }
}
static int leftKey3935(Ent3935* st) {
    int best = 0, found = 0;
    for (int i = 0; i < HS3935; i++) if (st[i].used) {
        if (!found || st[i].key < best) { best = st[i].key; found = 1; }
    }
    return best;
}
static int rightKey3935(Ent3935* st) {
    int best = 0, found = 0;
    for (int i = 0; i < HS3935; i++) if (st[i].used) {
        if (!found || st[i].key > best) { best = st[i].key; found = 1; }
    }
    return best;
}
static int qpow3935(long long a, int b) {
    long long ans = 1;
    while (b > 0) {
        if (b & 1) ans = ans * a % MOD3935;
        a = a * a % MOD3935;
        b >>= 1;
    }
    return (int)ans;
}

int* powerUpdate(int* nums, int numsSize, int p, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    memset(L3935, 0, sizeof(L3935));
    memset(R3935, 0, sizeof(R3935));
    sz1_3935 = 0; sz2_3935 = numsSize;
    for (int i = 0; i < numsSize; i++) merge3935(R3935, nums[i], 1);
    int* ans = malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int val = queries[qi][0], k = queries[qi][1];
        merge3935(R3935, val, 1); sz2_3935++;
        int node = leftKey3935(R3935);
        merge3935(R3935, node, -1); sz2_3935--;
        merge3935(L3935, node, 1); sz1_3935++;
        while (sz2_3935 < k) {
            node = rightKey3935(L3935);
            merge3935(L3935, node, -1); sz1_3935--;
            merge3935(R3935, node, 1); sz2_3935++;
        }
        while (sz2_3935 > k) {
            node = leftKey3935(R3935);
            merge3935(R3935, node, -1); sz2_3935--;
            merge3935(L3935, node, 1); sz1_3935++;
        }
        int x = leftKey3935(R3935);
        p = qpow3935(p, x);
        ans[qi] = p;
    }
    *returnSize = queriesSize;
    return ans;
}
