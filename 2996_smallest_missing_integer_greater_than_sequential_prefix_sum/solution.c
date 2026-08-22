// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int key;
    int used;
} HS2996;

static unsigned hash2996(int key) {
    unsigned x = (unsigned)key;
    x ^= x >> 16;
    x *= 0x7feb352dU;
    x ^= x >> 15;
    x *= 0x846ca68bU;
    x ^= x >> 16;
    return x;
}

static void hsAdd2996(HS2996* t, int cap, int key) {
    unsigned i = hash2996(key) & (unsigned)(cap - 1);
    while (t[i].used) {
        if (t[i].key == key) return;
        i = (i + 1) & (unsigned)(cap - 1);
    }
    t[i].used = 1;
    t[i].key = key;
}

static bool hsHas2996(HS2996* t, int cap, int key) {
    unsigned i = hash2996(key) & (unsigned)(cap - 1);
    while (t[i].used) {
        if (t[i].key == key) return true;
        i = (i + 1) & (unsigned)(cap - 1);
    }
    return false;
}

int missingInteger(int* nums, int numsSize) {
    int sum = nums[0];
    for (int i = 1; i < numsSize && nums[i] == nums[i - 1] + 1; i++) sum += nums[i];
    int cap = 1;
    while (cap < numsSize * 2 + 16) cap <<= 1;
    HS2996* seen = (HS2996*)calloc((size_t)cap, sizeof(HS2996));
    for (int i = 0; i < numsSize; i++) hsAdd2996(seen, cap, nums[i]);
    while (hsHas2996(seen, cap, sum)) sum++;
    free(seen);
    return sum;
}
