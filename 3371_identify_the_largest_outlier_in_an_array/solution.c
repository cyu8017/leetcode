// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

#include <stdlib.h>

typedef struct { int key, val, used; } HM;
static int hm_get(HM* t, int cap, int key) {
    unsigned h = (unsigned)key * 2654435761u % (unsigned)cap;
    for (;;) { if (!t[h].used) return 0; if (t[h].key == key) return t[h].val; h = (h + 1) % cap; }
}
static void hm_add(HM* t, int cap, int key, int d) {
    unsigned h = (unsigned)key * 2654435761u % (unsigned)cap;
    for (;;) {
        if (!t[h].used) { t[h].used = 1; t[h].key = key; t[h].val = d; return; }
        if (t[h].key == key) { t[h].val += d; return; }
        h = (h + 1) % cap;
    }
}

int getLargestOutlier(int* nums, int numsSize) {
    int cap = 1; while (cap < numsSize * 4 + 16) cap <<= 1;
    HM* freq = (HM*)calloc(cap, sizeof(HM));
    long long sum = 0;
    for (int i = 0; i < numsSize; i++) { sum += nums[i]; hm_add(freq, cap, nums[i], 1); }
    long long ans = -1000000000000000000LL;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        hm_add(freq, cap, x, -1);
        long long rem = sum - x;
        if (rem % 2 == 0) {
            int cand = (int)(rem / 2);
            if (hm_get(freq, cap, cand) > 0 && x > ans) ans = x;
        }
        hm_add(freq, cap, x, 1);
    }
    free(freq);
    return (int)ans;
}
