// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maximumBeauty(int* flowers, int flowersSize, long long newFlowers, int target, int full, int partial) {
    int n = flowersSize;
    for (int i = 0; i < n; i++) if (flowers[i] > target) flowers[i] = target;
    qsort(flowers, (size_t)n, sizeof(int), cmp_int);
    long long sum = 0;
    for (int i = 0; i < n; i++) sum += flowers[i];
    if ((long long)target * n - sum <= newFlowers) return (long long)n * full;
    long long* pref = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + flowers[i];
    long long ans = 0;
    int j = n - 1;
    long long remain = newFlowers;
    for (int complete = 0; complete <= n; complete++) {
        if (complete > 0) {
            long long need = target - flowers[n - complete];
            if (remain < need) break;
            remain -= need;
        }
        while (j >= n - complete || (j >= 0 && (long long)flowers[j] * (j + 1) - pref[j + 1] > remain)) j--;
        long long partialVal = 0;
        if (j >= 0) {
            long long extra = (remain - ((long long)flowers[j] * (j + 1) - pref[j + 1])) / (j + 1);
            partialVal = flowers[j] + extra;
            if (partialVal >= target) partialVal = target - 1;
        }
        long long cand = (long long)complete * full + partialVal * partial;
        if (cand > ans) ans = cand;
    }
    free(pref);
    return ans;
}
