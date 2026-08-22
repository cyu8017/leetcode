// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

#include <stdlib.h>

int largestRectangleArea(int* heights, int heightsSize) {
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
