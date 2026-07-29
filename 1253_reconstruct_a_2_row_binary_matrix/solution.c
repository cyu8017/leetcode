// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

#include <stdlib.h>
#include <string.h>

int** reconstructMatrix(int upper, int lower, int* colsum, int colsumSize, int* returnSize, int** returnColumnSizes) {
    int* top = (int*)calloc((size_t)colsumSize, sizeof(int));
    int* bottom = (int*)calloc((size_t)colsumSize, sizeof(int));
    for (int i = 0; i < colsumSize; i++) {
        if (colsum[i] == 2) {
            top[i] = bottom[i] = 1;
            upper--;
            lower--;
        }
    }
    if (upper < 0 || lower < 0) {
        free(top);
        free(bottom);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    for (int i = 0; i < colsumSize; i++) {
        if (colsum[i] == 1) {
            if (upper > 0) {
                top[i] = 1;
                upper--;
            } else if (lower > 0) {
                bottom[i] = 1;
                lower--;
            } else {
                free(top);
                free(bottom);
                *returnSize = 0;
                *returnColumnSizes = NULL;
                return NULL;
            }
        }
    }
    if (upper != 0 || lower != 0) {
        free(top);
        free(bottom);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int** ans = (int**)malloc(2 * sizeof(int*));
    ans[0] = top;
    ans[1] = bottom;
    *returnSize = 2;
    *returnColumnSizes = (int*)malloc(2 * sizeof(int));
    (*returnColumnSizes)[0] = colsumSize;
    (*returnColumnSizes)[1] = colsumSize;
    return ans;
}
