// LeetCode 0740 - Delete and Earn
// https://leetcode.com/problems/delete-and-earn/

#include <stdlib.h>

int deleteAndEarn(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0;
    }
    int maxNum = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > maxNum) {
            maxNum = nums[i];
        }
    }
    int* points = (int*)calloc((size_t)(maxNum + 1), sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        points[nums[i]] += nums[i];
    }
    int take = 0, skip = 0;
    for (int i = 0; i <= maxNum; i++) {
        int newTake = skip + points[i];
        int newSkip = skip > take ? skip : take;
        take = newTake;
        skip = newSkip;
    }
    free(points);
    return take > skip ? take : skip;
}
