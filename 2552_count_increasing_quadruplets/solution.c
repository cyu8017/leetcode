// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

#include <stdlib.h>
#include <string.h>

long long countQuadruplets(int* nums, int numsSize) {
    long long ans = 0;
    int* great = (int*)calloc((size_t)numsSize, sizeof(int));
    for (int j = 0; j < numsSize; j++) {
        for (int i = 0; i < j; i++) {
            if (nums[i] < nums[j]) ans += great[i];
            else if (nums[i] > nums[j]) great[i]++;
        }
    }
    free(great);
    return ans;
}
