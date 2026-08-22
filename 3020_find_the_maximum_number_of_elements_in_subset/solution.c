// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { long long key; int val; bool used; } HEnt;
static unsigned hash_ll(unsigned long long x) {
    x ^= x >> 30; x *= 0xbf58476d1ce4e5b9ULL; x ^= x >> 27; x *= 0x94d049bb133111ebULL; x ^= x >> 31;
    return (unsigned)x;
}
static void hinc(HEnt* t, int cap, long long key) {
    unsigned h = hash_ll((unsigned long long)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val++; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = 1;
}
static int hget(HEnt* t, int cap, long long key) {
    unsigned h = hash_ll((unsigned long long)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) return t[h].val;
        h = (h + 1) & (unsigned)(cap - 1);
    }
    return 0;
}

int maximumLength(int* nums, int numsSize) {
    int cap = 1;
    while (cap < numsSize * 2 + 16) cap <<= 1;
    HEnt* t = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    for (int i = 0; i < numsSize; i++) hinc(t, cap, nums[i]);
    int c1 = hget(t, cap, 1);
    int ans = c1 - ((c1 % 2) ^ 1);
    for (int i = 0; i < cap; i++) if (t[i].used && t[i].key != 1) {
        long long x = t[i].key;
        int tt = 0;
        while (hget(t, cap, x) > 1) {
            if (x > 1000000000LL / x) { tt += 2; x = x * x; break; }
            x = x * x;
            tt += 2;
        }
        if (hget(t, cap, x) > 0) tt += 1;
        else tt -= 1;
        if (tt > ans) ans = tt;
    }
    free(t);
    return ans;
}
