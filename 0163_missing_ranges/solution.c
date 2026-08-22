// LeetCode 0163 - Missing Ranges
#include <stdlib.h>
int** findMissingRanges(int* nums, int numsSize, int lower, int upper,
                        int* returnSize, int** returnColumnSizes) {
    int** result = malloc((numsSize + 1) * sizeof(*result));
    *returnColumnSizes = malloc((numsSize + 1) * sizeof(**returnColumnSizes));
    *returnSize = 0;
    long long prev = (long long)lower - 1;
    for (int i = 0; i <= numsSize; ++i) {
        long long current = i == numsSize ? (long long)upper + 1 : nums[i];
        if (current - prev >= 2) {
            result[*returnSize] = malloc(2 * sizeof(int));
            result[*returnSize][0] = (int)(prev + 1);
            result[*returnSize][1] = (int)(current - 1);
            (*returnColumnSizes)[(*returnSize)++] = 2;
        }
        prev = current;
    }
    return result;
}