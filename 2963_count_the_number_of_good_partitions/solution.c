// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

#include <stdlib.h>

typedef struct {
    int key;
    int val;
    int used;
} HM2963;

static unsigned hash2963(int key) {
    unsigned x = (unsigned)key;
    x ^= x >> 16;
    x *= 0x7feb352dU;
    x ^= x >> 15;
    x *= 0x846ca68bU;
    x ^= x >> 16;
    return x;
}

static void hmPut2963(HM2963* t, int cap, int key, int val) {
    unsigned i = hash2963(key) & (unsigned)(cap - 1);
    while (t[i].used) {
        if (t[i].key == key) {
            t[i].val = val;
            return;
        }
        i = (i + 1) & (unsigned)(cap - 1);
    }
    t[i].used = 1;
    t[i].key = key;
    t[i].val = val;
}

static int hmGet2963(HM2963* t, int cap, int key) {
    unsigned i = hash2963(key) & (unsigned)(cap - 1);
    while (t[i].used) {
        if (t[i].key == key) return t[i].val;
        i = (i + 1) & (unsigned)(cap - 1);
    }
    return -1;
}

int numberOfGoodPartitions(int* nums, int numsSize) {
    const int mod = 1000000007;
    int cap = 1;
    while (cap < numsSize * 2 + 16) cap <<= 1;
    HM2963* last = (HM2963*)calloc((size_t)cap, sizeof(HM2963));
    for (int i = 0; i < numsSize; i++) {
        hmPut2963(last, cap, nums[i], i);
    }
    int ans = 1;
    int end = 0;
    for (int i = 0; i < numsSize; i++) {
        int lv = hmGet2963(last, cap, nums[i]);
        if (lv > end) end = lv;
        if (i == end && i != numsSize - 1) {
            ans = (int)((ans * 2LL) % mod);
        }
    }
    free(last);
    return ans;
}
