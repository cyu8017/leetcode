// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

#include <stdlib.h>

static int cmp3180(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int *rv3180, n3180, *f3180;

static int lb3180(int x) {
    int lo = 0, hi = n3180;
    while (lo < hi) { int mid = (lo + hi) / 2; if (rv3180[mid] < x) lo = mid + 1; else hi = mid; }
    return lo;
}
static int dfs3180(int x) {
    if (f3180[x] != -1) return f3180[x];
    int i = lb3180(x + 1);
    f3180[x] = 0;
    for (int t = i; t < n3180; t++) {
        int v = rv3180[t] + dfs3180(x + rv3180[t]);
        if (v > f3180[x]) f3180[x] = v;
    }
    return f3180[x];
}

int maxTotalReward(int* rewardValues, int rewardValuesSize) {
    qsort(rewardValues, rewardValuesSize, sizeof(int), cmp3180);
    rv3180 = rewardValues; n3180 = rewardValuesSize;
    int sz = rewardValues[n3180 - 1] << 1;
    f3180 = malloc(sz * sizeof(int));
    for (int i = 0; i < sz; i++) f3180[i] = -1;
    int ans = dfs3180(0);
    free(f3180);
    return ans;
}
