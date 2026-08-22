// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

#include <stdlib.h>

int minOperations(int* nums, int numsSize, int k) {
    int* seen = (int*)calloc(numsSize, sizeof(int));
    int sn = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < k) { free(seen); return -1; }
        if (nums[i] > k) {
            int found = 0;
            for (int j = 0; j < sn; j++) if (seen[j] == nums[i]) { found = 1; break; }
            if (!found) seen[sn++] = nums[i];
        }
    }
    free(seen);
    return sn;
}
