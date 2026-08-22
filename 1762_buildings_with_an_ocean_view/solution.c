// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findBuildings(int* heights, int heightsSize, int* returnSize) {
    int* buffer = (int*)malloc(heightsSize * sizeof(int));
    int count = 0;
    int tallest = 0;
    for (int i = heightsSize - 1; i >= 0; i--) {
        if (heights[i] > tallest) {
            buffer[count++] = i;
            tallest = heights[i];
        }
    }
    int* ans = (int*)malloc(count * sizeof(int));
    for (int i = 0; i < count; i++) {
        ans[i] = buffer[count - 1 - i];
    }
    free(buffer);
    *returnSize = count;
    return ans;
}
