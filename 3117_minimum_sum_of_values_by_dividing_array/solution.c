// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

#include <stdlib.h>
#include <string.h>

enum { INF3117 = 1 << 29, HSIZE3117 = 1 << 18 };

typedef struct { long long key; int val; int used; } Ent3117;
static Ent3117* ht3117;
static int *nums3117, *and3117, n3117, m3117;

static int htget(long long key, int* found) {
    unsigned h = (unsigned)(key % HSIZE3117);
    for (int i = 0; i < HSIZE3117; i++) {
        unsigned j = (h + i) % HSIZE3117;
        if (!ht3117[j].used) { *found = 0; return (int)j; }
        if (ht3117[j].key == key) { *found = 1; return (int)j; }
    }
    *found = 0; return 0;
}

static int dfs3117(int i, int j, int a) {
    if (n3117 - i < m3117 - j) return INF3117;
    if (j == m3117) return i == n3117 ? 0 : INF3117;
    a &= nums3117[i];
    if (a < and3117[j]) return INF3117;
    long long key = ((long long)i << 36) | ((long long)j << 32) | (unsigned)a;
    int found, slot = htget(key, &found);
    if (found) return ht3117[slot].val;
    int ans = dfs3117(i + 1, j, a);
    if (a == and3117[j]) {
        int t = dfs3117(i + 1, j + 1, -1) + nums3117[i];
        if (t < ans) ans = t;
    }
    ht3117[slot].used = 1; ht3117[slot].key = key; ht3117[slot].val = ans;
    return ans;
}

int minimumValueSum(int* nums, int numsSize, int* andValues, int andValuesSize) {
    nums3117 = nums; and3117 = andValues; n3117 = numsSize; m3117 = andValuesSize;
    ht3117 = calloc(HSIZE3117, sizeof(Ent3117));
    int ans = dfs3117(0, 0, -1);
    free(ht3117);
    return ans < INF3117 ? ans : -1;
}
