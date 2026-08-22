// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

#include <limits.h>
#include <stdlib.h>

static int min_int(int a, int b) {
    return a < b ? a : b;
}

int minCostII(int** costs, int costsSize, int* costsColSize) {
    if (costsSize == 0) {
        return 0;
    }
    int colorCount = costsColSize[0];
    int* previous = (int*)malloc((size_t)colorCount * sizeof(int));
    for (int i = 0; i < colorCount; i++) {
        previous[i] = costs[0][i];
    }
    for (int row = 1; row < costsSize; row++) {
        int minCost = previous[0];
        int minIndex = 0;
        for (int color = 1; color < colorCount; color++) {
            if (previous[color] < minCost) {
                minCost = previous[color];
                minIndex = color;
            }
        }
        int secondMin = INT_MAX;
        for (int color = 0; color < colorCount; color++) {
            if (color != minIndex && previous[color] < secondMin) {
                secondMin = previous[color];
            }
        }
        int* current = (int*)malloc((size_t)colorCount * sizeof(int));
        for (int color = 0; color < colorCount; color++) {
            int extra = color == minIndex ? secondMin : minCost;
            current[color] = costs[row][color] + extra;
        }
        free(previous);
        previous = current;
    }
    int result = previous[0];
    for (int color = 1; color < colorCount; color++) {
        result = min_int(result, previous[color]);
    }
    free(previous);
    return result;
}
