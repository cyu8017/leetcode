// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

#include <stdlib.h>

int** imageSmoother(int** img, int imgSize, int* imgColSize, int* returnSize, int** returnColumnSizes) {
    int m = imgSize, n = imgColSize[0];
    int** result = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        result[i] = (int*)malloc((size_t)n * sizeof(int));
        (*returnColumnSizes)[i] = n;
        for (int j = 0; j < n; j++) {
            int sum = 0, count = 0;
            for (int x = i - 1; x <= i + 1; x++) {
                for (int y = j - 1; y <= j + 1; y++) {
                    if (x >= 0 && x < m && y >= 0 && y < n) {
                        sum += img[x][y];
                        count++;
                    }
                }
            }
            result[i][j] = sum / count;
        }
    }
    *returnSize = m;
    return result;
}
