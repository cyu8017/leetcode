// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

#include <stdlib.h>
#include <stdbool.h>

static bool isSelfDividing(int num) {
    int x = num;
    while (x) {
        int digit = x % 10;
        if (digit == 0 || num % digit != 0) {
            return false;
        }
        x /= 10;
    }
    return true;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* selfDividingNumbers(int left, int right, int* returnSize) {
    int* result = (int*)malloc((size_t)(right - left + 1) * sizeof(int));
    int size = 0;
    for (int num = left; num <= right; num++) {
        if (isSelfDividing(num)) {
            result[size++] = num;
        }
    }
    *returnSize = size;
    return result;
}
