// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

#include <stdlib.h>

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

typedef struct { int g, idx; } Pair;

long long maxGcdSum(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long* pref = (long long*)malloc((n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    long long ans = 0;
    Pair* st = (Pair*)malloc((n + 1) * sizeof(Pair));
    int sn = 0;
    for (int i = 0; i < n; i++) {
        Pair* nst = (Pair*)malloc((sn + 2) * sizeof(Pair));
        int nn = 0;
        nst[nn++] = (Pair){nums[i], i};
        for (int j = 0; j < sn; j++) {
            int g = gcd(st[j].g, nums[i]);
            if (nst[nn - 1].g == g) continue;
            nst[nn++] = (Pair){g, st[j].idx};
        }
        free(st); st = nst; sn = nn;
        for (int j = 0; j < sn; j++) {
            if (i - st[j].idx + 1 >= k) {
                long long cand = (pref[i + 1] - pref[st[j].idx]) * st[j].g;
                if (cand > ans) ans = cand;
            }
        }
    }
    free(st); free(pref);
    return ans;
}
