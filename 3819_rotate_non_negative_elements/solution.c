// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

#include <stdlib.h>

int* rotateElements(int* nums, int numsSize, int k, int* returnSize) {
    int* t = (int*)malloc((size_t)numsSize * sizeof(int));
    int m = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] >= 0) t[m++] = nums[i];
    int* d = (int*)malloc((size_t)(m ? m : 1) * sizeof(int));
    if (m > 0) {
        for (int i = 0; i < m; i++) {
            int idx = ((i - k) % m + m) % m;
            d[idx] = t[i];
        }
        int j = 0;
        for (int i = 0; i < numsSize; i++) if (nums[i] >= 0) nums[i] = d[j++];
    }
    free(t); free(d);
    *returnSize = numsSize;
    return nums;
}
