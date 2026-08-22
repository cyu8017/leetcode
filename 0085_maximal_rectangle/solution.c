// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

#include <stdlib.h>
#include <string.h>

static int largestHistogram(int* heights, int heightsSize) {
    int* stack = (int*)malloc((size_t)(heightsSize + 1) * sizeof(int));
    int top = -1;
    int maxArea = 0;

    for (int i = 0; i <= heightsSize; i++) {
        int height = i == heightsSize ? 0 : heights[i];
        while (top >= 0 && heights[stack[top]] > height) {
            int h = heights[stack[top--]];
            int width = top < 0 ? i : i - stack[top] - 1;
            int area = h * width;
            if (area > maxArea) {
                maxArea = area;
            }
        }
        stack[++top] = i;
    }

    free(stack);
    return maxArea;
}

int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) {
        return 0;
    }

    int cols = matrixColSize[0];
    int* heights = (int*)calloc((size_t)cols, sizeof(int));
    int maxArea = 0;

    for (int r = 0; r < matrixSize; r++) {
        for (int j = 0; j < cols; j++) {
            heights[j] = matrix[r][j] == '1' ? heights[j] + 1 : 0;
        }
        int area = largestHistogram(heights, cols);
        if (area > maxArea) {
            maxArea = area;
        }
    }

    free(heights);
    return maxArea;
}
