// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

#include <stdlib.h>

int numSubmat(int** mat, int matSize, int* matColSize) {
    int cols = matColSize[0];
    int* heights = (int*)calloc((size_t)cols, sizeof(int));
    int ans = 0;
    for (int r = 0; r < matSize; r++) {
        for (int j = 0; j < cols; j++) {
            heights[j] = mat[r][j] ? heights[j] + 1 : 0;
        }
        int* stackH = (int*)malloc((size_t)cols * sizeof(int));
        int* stackW = (int*)malloc((size_t)cols * sizeof(int));
        int top = 0;
        int running = 0;
        for (int j = 0; j < cols; j++) {
            int h = heights[j];
            int count = 1;
            while (top > 0 && stackH[top - 1] >= h) {
                top--;
                running -= stackH[top] * stackW[top];
                count += stackW[top];
            }
            stackH[top] = h;
            stackW[top] = count;
            top++;
            running += h * count;
            ans += running;
        }
        free(stackH);
        free(stackW);
    }
    free(heights);
    return ans;
}
