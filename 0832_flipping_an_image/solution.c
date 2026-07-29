// LeetCode 0832 - Flipping an Image
// https://leetcode.com/problems/flipping-an-image/

#include <stdlib.h>

int** flipAndInvertImage(int** image, int imageSize, int* imageColSize, int* returnSize, int** returnColumnSizes) {
    int n = imageColSize[0];
    int** ans = (int**)malloc((size_t)imageSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)imageSize * sizeof(int));
    for (int r = 0; r < imageSize; r++) {
        ans[r] = (int*)malloc((size_t)n * sizeof(int));
        (*returnColumnSizes)[r] = n;
        for (int c = 0; c < n; c++)
            ans[r][c] = 1 - image[r][n - 1 - c];
    }
    *returnSize = imageSize;
    return ans;
}
