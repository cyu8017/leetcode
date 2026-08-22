// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

#include <stdlib.h>

int minOperations(int* nums, int numsSize, int* target, int targetSize) {
    (void)targetSize;
    int* keys = (int*)malloc((size_t)numsSize * sizeof(int));
    int ksz = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != target[i]) {
            int found = 0;
            for (int j = 0; j < ksz; j++) if (keys[j] == nums[i]) { found = 1; break; }
            if (!found) keys[ksz++] = nums[i];
        }
    }
    free(keys);
    return ksz;
}
