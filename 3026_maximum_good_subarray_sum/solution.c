// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

typedef struct { int key; long long val; bool used; } HEnt;
static unsigned hash_u(unsigned x) { x ^= x >> 16; x *= 0x7feb352dU; x ^= x >> 15; x *= 0x846ca68bU; x ^= x >> 16; return x; }
static bool hget(HEnt* t, int cap, int key, long long* out) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { *out = t[h].val; return true; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    return false;
}
static void hset_min(HEnt* t, int cap, int key, long long val) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) {
            if (val < t[h].val) t[h].val = val;
            return;
        }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = val;
}

long long maximumSubarraySum(int* nums, int numsSize, int k) {
    int cap = 1;
    while (cap < numsSize * 2 + 16) cap <<= 1;
    HEnt* p = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    hset_min(p, cap, nums[0], 0);
    long long s = 0, ans = LLONG_MIN;
    for (int i = 0; i < numsSize; i++) {
        s += nums[i];
        long long t;
        if (hget(p, cap, nums[i] - k, &t) && s - t > ans) ans = s - t;
        if (hget(p, cap, nums[i] + k, &t) && s - t > ans) ans = s - t;
        if (i + 1 == numsSize) break;
        hset_min(p, cap, nums[i + 1], s);
    }
    free(p);
    return ans == LLONG_MIN ? 0 : ans;
}
