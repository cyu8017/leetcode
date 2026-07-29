// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

#include <stdlib.h>

int minSwaps(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int* zeros = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = gridColSize[i] - 1; j >= 0; j--) {
            if (grid[i][j]) break;
            count++;
        }
        zeros[i] = count;
    }
    int answer = 0;
    for (int i = 0; i < n; i++) {
        int required = n - i - 1;
        int j = i;
        while (j < n && zeros[j] < required) j++;
        if (j == n) {
            free(zeros);
            return -1;
        }
        answer += j - i;
        int val = zeros[j];
        for (int k = j; k > i; k--) zeros[k] = zeros[k - 1];
        zeros[i] = val;
    }
    free(zeros);
    return answer;
}
