// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

#include <stdlib.h>

int maxFixedPoints(int* nums, int numsSize) {
    int* tails = malloc((size_t)numsSize * sizeof(int));
    int tn = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (i < x) continue;
        int d = i - x;
        int lo = 0, hi = tn;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (tails[mid] >= d) hi = mid;
            else lo = mid + 1;
        }
        if (lo == tn) tails[tn++] = d;
        else tails[lo] = d;
    }
    free(tails);
    return tn;
}
