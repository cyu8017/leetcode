// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

#include <stdlib.h>

int* findValidElements(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* right = malloc((size_t)n * sizeof(int));
    right[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) right[i] = right[i + 1] > nums[i] ? right[i + 1] : nums[i];
    int left = 0;
    int* ans = malloc((size_t)n * sizeof(int));
    int an = 0;
    for (int i = 0; i < n; i++) {
        int x = nums[i];
        if (x > left || i == n - 1 || x > right[i + 1]) ans[an++] = x;
        if (x > left) left = x;
    }
    free(right);
    *returnSize = an;
    return ans;
}
