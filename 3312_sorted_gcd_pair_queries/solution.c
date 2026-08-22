// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

#include <stdlib.h>

int* gcdValues(int* nums, int numsSize, long long* queries, int queriesSize, int* returnSize) {
    int maxV = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxV) maxV = nums[i];
    int* cnt = (int*)calloc((size_t)(maxV + 1), sizeof(int));
    for (int i = 0; i < numsSize; i++) cnt[nums[i]]++;
    long long* divCnt = (long long*)calloc((size_t)(maxV + 1), sizeof(long long));
    for (int g = 1; g <= maxV; g++) {
        long long c = 0;
        for (int m = g; m <= maxV; m += g) c += cnt[m];
        divCnt[g] = c * (c - 1) / 2;
    }
    long long* exact = (long long*)calloc((size_t)(maxV + 1), sizeof(long long));
    for (int g = maxV; g >= 1; g--) {
        exact[g] = divCnt[g];
        for (int m = 2 * g; m <= maxV; m += g) exact[g] -= exact[m];
    }
    long long* pref = (long long*)calloc((size_t)(maxV + 1), sizeof(long long));
    for (int g = 1; g <= maxV; g++) pref[g] = pref[g - 1] + exact[g];
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        long long q = queries[i];
        int lo = 1, hi = maxV;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (pref[mid] > q) hi = mid;
            else lo = mid + 1;
        }
        ans[i] = lo;
    }
    free(cnt); free(divCnt); free(exact); free(pref);
    *returnSize = queriesSize;
    return ans;
}
