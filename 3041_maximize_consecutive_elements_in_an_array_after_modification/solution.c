// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int key, val; bool used; } HEnt;
static unsigned hash_u(unsigned x) { x ^= x >> 16; x *= 0x7feb352dU; x ^= x >> 15; x *= 0x846ca68bU; x ^= x >> 16; return x; }
static int hget(HEnt* t, int cap, int key) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) return t[h].val;
        h = (h + 1) & (unsigned)(cap - 1);
    }
    return 0;
}
static void hset(HEnt* t, int cap, int key, int val) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val = val; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = val;
}
static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

int maxSelectedElements(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int cap = 1;
    while (cap < numsSize * 4 + 16) cap <<= 1;
    HEnt* dp = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        int v1 = hget(dp, cap, num) + 1;
        int v0 = hget(dp, cap, num - 1) + 1;
        hset(dp, cap, num + 1, v1);
        hset(dp, cap, num, v0);
        if (v0 > ans) ans = v0;
        if (v1 > ans) ans = v1;
    }
    free(dp);
    return ans;
}
