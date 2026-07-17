// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

#include <stdlib.h>

int minElements(int* nums, int numsSize, int limit, int goal) {
    long long sum = 0;
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
    }
    long long diff = sum - goal;
    if (diff < 0) {
        diff = -diff;
    }
    return (int)((diff + limit - 1) / limit);
}
