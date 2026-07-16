// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char* format_range(int start, int end) {
    if (start == end) {
        char buffer[32];
        snprintf(buffer, sizeof(buffer), "%d", start);
        return strdup(buffer);
    }
    char buffer[64];
    snprintf(buffer, sizeof(buffer), "%d->%d", start, end);
    return strdup(buffer);
}

char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    *returnSize = 0;
    if (numsSize == 0) {
        return NULL;
    }

    int capacity = 8;
    char** result = malloc((size_t)capacity * sizeof(char*));
    int index = 0;

    while (index < numsSize) {
        int start = nums[index];
        while (index + 1 < numsSize && nums[index + 1] == nums[index] + 1) {
            index++;
        }
        if (*returnSize == capacity) {
            capacity *= 2;
            result = realloc(result, (size_t)capacity * sizeof(char*));
        }
        result[*returnSize] = format_range(start, nums[index]);
        (*returnSize)++;
        index++;
    }

    return result;
}
