// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

#include <stdlib.h>

static int abs2613(int x) { return x < 0 ? -x : x; }

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* beautifulPair(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    (void)nums2Size;
    int n = nums1Size;
    long long bestDist = 1000000000000000000LL;
    int ai = 0, aj = 1;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            long long d = (long long)abs2613(nums1[i] - nums1[j]) + abs2613(nums2[i] - nums2[j]);
            if (d < bestDist || (d == bestDist && (i < ai || (i == ai && j < aj)))) {
                bestDist = d;
                ai = i; aj = j;
            }
        }
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = ai; ans[1] = aj;
    *returnSize = 2;
    return ans;
}
