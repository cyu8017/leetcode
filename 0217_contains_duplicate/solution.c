// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int compareInts(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

bool containsDuplicate(int* nums, int numsSize) {
    if (numsSize <= 1) {
        return false;
    }
    int* copy = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(copy, nums, (size_t)numsSize * sizeof(int));
    qsort(copy, (size_t)numsSize, sizeof(int), compareInts);
    for (int i = 1; i < numsSize; i++) {
        if (copy[i] == copy[i - 1]) {
            free(copy);
            return true;
        }
    }
    free(copy);
    return false;
}
