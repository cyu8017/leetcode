// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

#include <stdlib.h>

#define MOD2031 1000000007

typedef struct { int* bit; int n; } Fen2031;

static Fen2031* fenNew(int n) {
    Fen2031* f = (Fen2031*)malloc(sizeof(Fen2031));
    f->n = n + 2;
    f->bit = (int*)calloc((size_t)f->n, sizeof(int));
    return f;
}

static void fenAdd(Fen2031* f, int i, int v) {
    for (; i < f->n; i += i & -i) f->bit[i] += v;
}

static int fenSum(Fen2031* f, int i) {
    int s = 0;
    for (; i > 0; i -= i & -i) s += f->bit[i];
    return s;
}

int subarraysWithMoreZerosThanOnes(int* nums, int numsSize) {
    int n = numsSize;
    int offset = n + 1;
    Fen2031* fw = fenNew(2 * n + 5);
    int pref = 0;
    fenAdd(fw, offset, 1);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == 1) pref++; else pref--;
        int idx = pref + offset;
        ans = (ans + fenSum(fw, idx - 1)) % MOD2031;
        fenAdd(fw, idx, 1);
    }
    free(fw->bit); free(fw);
    return ans;
}
