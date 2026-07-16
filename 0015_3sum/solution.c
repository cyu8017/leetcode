// LeetCode 0015 - 3Sum
// https://leetcode.com/problems/3sum/

#include <stdlib.h>

static int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), cmp);

    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int count = 0;

    for (int i = 0; i < numsSize - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }

        int left = i + 1;
        int right = numsSize - 1;
        while (left < right) {
            int total = nums[i] + nums[left] + nums[right];
            if (total == 0) {
                if (count >= capacity) {
                    capacity *= 2;
                    result = (int**)realloc(result, (size_t)capacity * sizeof(int*));
                    colSizes = (int*)realloc(colSizes, (size_t)capacity * sizeof(int));
                }
                result[count] = (int*)malloc(3 * sizeof(int));
                result[count][0] = nums[i];
                result[count][1] = nums[left];
                result[count][2] = nums[right];
                colSizes[count] = 3;
                count++;

                while (left < right && nums[left] == nums[left + 1]) {
                    left++;
                }
                while (left < right && nums[right] == nums[right - 1]) {
                    right--;
                }
                left++;
                right--;
            } else if (total < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
