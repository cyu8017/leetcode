// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

#include <stdlib.h>

int* fallingSquares(int** positions, int positionsSize, int* positionsColSize, int* returnSize) {
    (void)positionsColSize;
    int* lefts = (int*)malloc((size_t)positionsSize * sizeof(int));
    int* rights = (int*)malloc((size_t)positionsSize * sizeof(int));
    int* heights = (int*)malloc((size_t)positionsSize * sizeof(int));
    int* answer = (int*)malloc((size_t)positionsSize * sizeof(int));
    int count = 0, maxHeight = 0;
    for (int i = 0; i < positionsSize; i++) {
        int L = positions[i][0], side = positions[i][1], R = L + side;
        int base = 0;
        for (int j = 0; j < count; j++) {
            if (rights[j] > L && lefts[j] < R && heights[j] > base) base = heights[j];
        }
        int h = base + side;
        lefts[count] = L; rights[count] = R; heights[count] = h; count++;
        if (h > maxHeight) maxHeight = h;
        answer[i] = maxHeight;
    }
    free(lefts); free(rights); free(heights);
    *returnSize = positionsSize;
    return answer;
}
