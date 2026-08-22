// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int* answer = (int*)calloc((size_t)temperaturesSize, sizeof(int));
    int* stack = (int*)malloc((size_t)temperaturesSize * sizeof(int));
    int top = 0;
    for (int i = 0; i < temperaturesSize; i++) {
        while (top > 0 && temperatures[stack[top - 1]] < temperatures[i]) {
            int prev = stack[--top];
            answer[prev] = i - prev;
        }
        stack[top++] = i;
    }
    free(stack);
    *returnSize = temperaturesSize;
    return answer;
}
