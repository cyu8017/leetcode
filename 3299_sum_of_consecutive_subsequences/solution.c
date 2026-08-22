// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

#include <stdlib.h>

/* sparse map via parallel arrays; values in nums range typically small - use hash open addressing */
typedef struct { int key, cnt, sum; int used; } Ent;

static Ent* findEnt(Ent* tab, int cap, int key, int create) {
    unsigned h = (unsigned)key * 2654435761u % (unsigned)cap;
    for (int i = 0; i < cap; i++) {
        unsigned idx = (h + i) % (unsigned)cap;
        if (!tab[idx].used) {
            if (!create) return NULL;
            tab[idx].used = 1; tab[idx].key = key; tab[idx].cnt = 0; tab[idx].sum = 0;
            return &tab[idx];
        }
        if (tab[idx].key == key) return &tab[idx];
    }
    return NULL;
}

int rangeSum(int* nums, int numsSize) {
    const int mod = 1000000007;
    int cap = 4096;
    Ent* tab = (Ent*)calloc((size_t)cap, sizeof(Ent));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        Ent* eL = findEnt(tab, cap, x - 1, 0);
        Ent* eR = findEnt(tab, cap, x + 1, 0);
        int cL = eL ? eL->cnt : 0, sL = eL ? eL->sum : 0;
        int cR = eR ? eR->cnt : 0, sR = eR ? eR->sum : 0;
        int c = (1 + cL + cR) % mod;
        int s = (int)(((long long)x + sL + (long long)cL * x % mod + sR + (long long)cR * x % mod) % mod);
        if (cL > 0 && cR > 0) {
            c = (int)((c + (long long)cL * cR % mod) % mod);
            s = (int)((s + (long long)sL * cR % mod + (long long)sR * cL % mod + (long long)cL * cR % mod * x % mod) % mod);
        }
        Ent* e = findEnt(tab, cap, x, 1);
        e->cnt = (e->cnt + c) % mod;
        e->sum = (e->sum + s) % mod;
        ans = (ans + s) % mod;
    }
    free(tab);
    return ans;
}
