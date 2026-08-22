// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
static int cmpK;
static int cmpRows(const void* a, const void* b) {
    int* ra = *(int**)a;
    int* rb = *(int**)b;
    return rb[cmpK] - ra[cmpK];
}

int** sortTheStudents(int** score, int scoreSize, int* scoreColSize, int k, int* returnSize, int** returnColumnSizes) {
    cmpK = k;
    qsort(score, (size_t)scoreSize, sizeof(int*), cmpRows);
    *returnSize = scoreSize;
    *returnColumnSizes = (int*)malloc((size_t)scoreSize * sizeof(int));
    for (int i = 0; i < scoreSize; i++) (*returnColumnSizes)[i] = scoreColSize[i];
    return score;
}
