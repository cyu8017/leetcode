// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long minOperations(int* nums, int numsSize, int k) {
    long long ans = 1LL << 62;
    int* sub = (int*)malloc(k * sizeof(int));
    for (int i = 0; i + k <= numsSize; i++) {
        memcpy(sub, nums + i, k * sizeof(int));
        qsort(sub, k, sizeof(int), cmp_int);
        int med = sub[k / 2];
        long long cost = 0;
        for (int j = 0; j < k; j++) {
            long long d = sub[j] - med; if (d < 0) d = -d; cost += d;
        }
        if (cost < ans) ans = cost;
    }
    free(sub);
    return ans;
}
