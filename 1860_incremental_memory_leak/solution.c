// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* memLeak(int memory1, int memory2, int* returnSize) {
    int second = 1;
    while (memory1 >= second || memory2 >= second) {
        if (memory1 >= memory2) memory1 -= second;
        else memory2 -= second;
        second++;
    }
    int* result = (int*)malloc(3 * sizeof(int));
    result[0] = second;
    result[1] = memory1;
    result[2] = memory2;
    *returnSize = 3;
    return result;
}
