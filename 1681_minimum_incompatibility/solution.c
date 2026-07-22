// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

#include <stdlib.h>

static int popcount(int x) {
    int c = 0;
    while (x) { c += x & 1; x >>= 1; }
    return c;
}

int minimumIncompatibility(int* nums, int numsSize, int k) {
    int n = numsSize;
    int size = n / k;
    int full = (1 << n) - 1;
    int* groups = (int*)malloc((size_t)(1 << n) * sizeof(int));
    int* gcost = (int*)malloc((size_t)(1 << n) * sizeof(int));
    int gcount = 0;
    for (int mask = 0; mask <= full; mask++) {
        if (popcount(mask) != size) continue;
        int seen[17] = {0};
        int mn = 20, mx = 0, ok = 1;
        for (int i = 0; i < n; i++) if (mask & (1 << i)) {
            if (seen[nums[i]]) { ok = 0; break; }
            seen[nums[i]] = 1;
            if (nums[i] < mn) mn = nums[i];
            if (nums[i] > mx) mx = nums[i];
        }
        if (!ok) continue;
        groups[gcount] = mask;
        gcost[gcount] = mx - mn;
        gcount++;
    }
    const int INF = 1000000000;
    int* memo = (int*)malloc((size_t)(1 << n) * sizeof(int));
    for (int i = 0; i <= full; i++) memo[i] = INF;
    memo[0] = 0;
    for (int mask = 0; mask <= full; mask++) {
        if (memo[mask] >= INF) continue;
        int first = -1;
        for (int i = 0; i < n; i++) if (!(mask & (1 << i))) { first = i; break; }
        if (first < 0) continue;
        for (int gi = 0; gi < gcount; gi++) {
            int g = groups[gi];
            if ((g & (1 << first)) && !(g & mask)) {
                int nm = mask | g;
                int cost = memo[mask] + gcost[gi];
                if (cost < memo[nm]) memo[nm] = cost;
            }
        }
    }
    int ans = memo[full] >= INF ? -1 : memo[full];
    free(groups); free(gcost); free(memo);
    return ans;
}
