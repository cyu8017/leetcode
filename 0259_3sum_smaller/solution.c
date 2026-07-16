// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

#include <stdlib.h>

static int compare_ints(const void* left, const void* right) {
    int a = *(const int*)left;
    int b = *(const int*)right;
    return a - b;
}

int threeSumSmaller(int* nums, int numsSize, int target) {
    qsort(nums, (size_t)numsSize, sizeof(int), compare_ints);
    int count = 0;
    for (int index = 0; index < numsSize - 2; index++) {
        int left = index + 1;
        int right = numsSize - 1;
        while (left < right) {
            int total = nums[index] + nums[left] + nums[right];
            if (total < target) {
                count += right - left;
                left++;
            } else {
                right--;
            }
        }
    }
    return count;
}
