// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

#include <stdlib.h>
#include <stdbool.h>

int findFinalValue(int* nums, int numsSize, int original) {
    int maxv = original;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxv) maxv = nums[i];
    bool* have = (bool*)calloc((size_t)maxv + 1, sizeof(bool));
    for (int i = 0; i < numsSize; i++) have[nums[i]] = true;
    while (original <= maxv && have[original]) original *= 2;
    free(have);
    return original;
}
