// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

#include <stdlib.h>

long long* kthSmallestEven(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* evenPrefix = calloc((size_t)(numsSize + 1), sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        evenPrefix[i + 1] = evenPrefix[i];
        if (nums[i] % 2 == 0) evenPrefix[i + 1]++;
    }
    long long* ans = malloc((size_t)queriesSize * sizeof(long long));
    for (int qi = 0; qi < queriesSize; qi++) {
        int l = queries[qi][0], r = queries[qi][1];
        long long k = queries[qi][2];
        long long lo = 1, hi = k + (r - l + 1);
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            int pos = 0;
            /* first i with nums[i] > 2*mid */
            int lo2 = 0, hi2 = numsSize;
            while (lo2 < hi2) {
                int m2 = (lo2 + hi2) / 2;
                if ((long long)nums[m2] > 2 * mid) hi2 = m2;
                else lo2 = m2 + 1;
            }
            pos = lo2;
            if (pos > r + 1) pos = r + 1;
            int removed = 0;
            if (pos > l) removed = evenPrefix[pos] - evenPrefix[l];
            if (mid - removed >= k) hi = mid;
            else lo = mid + 1;
        }
        ans[qi] = 2 * lo;
    }
    free(evenPrefix);
    *returnSize = queriesSize;
    return ans;
}
