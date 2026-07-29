// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int triangleNumber(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    int count = 0;
    for (int k = numsSize - 1; k >= 2; k--) {
        int i = 0, j = k - 1;
        while (i < j) {
            if (nums[i] + nums[j] > nums[k]) {
                count += j - i;
                j--;
            } else {
                i++;
            }
        }
    }
    return count;
}
