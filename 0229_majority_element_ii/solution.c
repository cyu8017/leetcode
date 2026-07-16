// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

#include <stdlib.h>

int* majorityElement(int* nums, int numsSize, int* returnSize) {
    int hasCandidate1 = 0;
    int hasCandidate2 = 0;
    int candidate1 = 0;
    int candidate2 = 0;
    int count1 = 0;
    int count2 = 0;

    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        if (hasCandidate1 && num == candidate1) {
            count1++;
        } else if (hasCandidate2 && num == candidate2) {
            count2++;
        } else if (count1 == 0) {
            candidate1 = num;
            hasCandidate1 = 1;
            count1 = 1;
        } else if (count2 == 0) {
            candidate2 = num;
            hasCandidate2 = 1;
            count2 = 1;
        } else {
            count1--;
            count2--;
        }
    }

    count1 = 0;
    count2 = 0;
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        if (hasCandidate1 && num == candidate1) {
            count1++;
        } else if (hasCandidate2 && num == candidate2) {
            count2++;
        }
    }

    int threshold = numsSize / 3;
    int capacity = 2;
    int* result = malloc((size_t)capacity * sizeof(int));
    *returnSize = 0;

    if (count1 > threshold) {
        result[(*returnSize)++] = candidate1;
    }
    if (hasCandidate2 && (!hasCandidate1 || candidate2 != candidate1) && count2 > threshold) {
        result[(*returnSize)++] = candidate2;
    }

    return result;
}
