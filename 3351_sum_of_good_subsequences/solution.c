// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

#include <stdlib.h>

/* open addressing hash map int->int */
typedef struct { int key, val; int used; } HM;
static int hm_get(HM* t, int cap, int key) {
    unsigned h = (unsigned)key * 2654435761u % (unsigned)cap;
    for (;;) {
        if (!t[h].used) return 0;
        if (t[h].key == key) return t[h].val;
        h = (h + 1) % cap;
    }
}
static void hm_add(HM* t, int cap, int key, int delta, int mod) {
    unsigned h = (unsigned)key * 2654435761u % (unsigned)cap;
    for (;;) {
        if (!t[h].used) { t[h].used = 1; t[h].key = key; t[h].val = (delta % mod + mod) % mod; return; }
        if (t[h].key == key) { t[h].val = (t[h].val + delta) % mod; return; }
        h = (h + 1) % cap;
    }
}

int sumOfGoodSubsequences(int* nums, int numsSize) {
    const int mod = 1000000007;
    int cap = 1;
    while (cap < numsSize * 4 + 16) cap <<= 1;
    HM* cnt = (HM*)calloc(cap, sizeof(HM));
    HM* sum = (HM*)calloc(cap, sizeof(HM));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int c = 1, s = x;
        int c1 = hm_get(cnt, cap, x - 1);
        if (c1 > 0) {
            c = (c + c1) % mod;
            s = (int)(((long long)s + hm_get(sum, cap, x - 1) + (long long)c1 * x) % mod);
        }
        int c2 = hm_get(cnt, cap, x + 1);
        if (c2 > 0) {
            c = (c + c2) % mod;
            s = (int)(((long long)s + hm_get(sum, cap, x + 1) + (long long)c2 * x) % mod);
        }
        hm_add(cnt, cap, x, c, mod);
        hm_add(sum, cap, x, s, mod);
        ans = (ans + s) % mod;
    }
    free(cnt); free(sum);
    return ans;
}
