// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

#include <stdlib.h>

int* canSeePersonsCount(int* heights, int heightsSize, int* returnSize) {
    int* ans = (int*)calloc((size_t)heightsSize, sizeof(int));
    int* stack = (int*)malloc((size_t)heightsSize * sizeof(int));
    int top = 0;
    for (int i = heightsSize - 1; i >= 0; i--) {
        int count = 0;
        while (top > 0 && heights[i] > stack[top - 1]) {
            top--;
            count++;
        }
        if (top > 0) count++;
        ans[i] = count;
        stack[top++] = heights[i];
    }
    free(stack);
    *returnSize = heightsSize;
    return ans;
}
