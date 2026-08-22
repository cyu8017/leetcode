// LeetCode 0370 - Range Addition
// https://leetcode.com/problems/range-addition/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getModifiedArray(int length, int** updates, int updatesSize, int* updatesColSize, int* returnSize) {
    (void)updatesColSize;
    int* diff = (int*)calloc((size_t)length + 1, sizeof(int));

    for (int index = 0; index < updatesSize; index++) {
        int start = updates[index][0];
        int end = updates[index][1];
        int inc = updates[index][2];
        diff[start] += inc;
        if (end + 1 < length + 1) {
            diff[end + 1] -= inc;
        }
    }

    int* result = (int*)malloc((size_t)length * sizeof(int));
    int running = 0;
    for (int index = 0; index < length; index++) {
        running += diff[index];
        result[index] = running;
    }

    free(diff);
    *returnSize = length;
    return result;
}
