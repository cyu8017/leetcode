// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

#include <stdlib.h>

static int compareInts(const void* left, const void* right) {
    return (*(const int*)left) - (*(const int*)right);
}

int minTotalDistance(int** grid, int gridSize, int* gridColSize) {
    int rowCapacity = 64;
    int colCapacity = 64;
    int rowCount = 0;
    int colCount = 0;
    int* rows = (int*)malloc((size_t)rowCapacity * sizeof(int));
    int* cols = (int*)malloc((size_t)colCapacity * sizeof(int));

    for (int rowIndex = 0; rowIndex < gridSize; rowIndex++) {
        for (int colIndex = 0; colIndex < gridColSize[rowIndex]; colIndex++) {
            if (grid[rowIndex][colIndex] == 1) {
                if (rowCount == rowCapacity) {
                    rowCapacity *= 2;
                    rows = (int*)realloc(rows, (size_t)rowCapacity * sizeof(int));
                }
                if (colCount == colCapacity) {
                    colCapacity *= 2;
                    cols = (int*)realloc(cols, (size_t)colCapacity * sizeof(int));
                }
                rows[rowCount++] = rowIndex;
                cols[colCount++] = colIndex;
            }
        }
    }

    qsort(cols, (size_t)colCount, sizeof(int), compareInts);
    int rowMedian = rows[rowCount / 2];
    int colMedian = cols[colCount / 2];

    int total = 0;
    for (int index = 0; index < rowCount; index++) {
        total += abs(rows[index] - rowMedian);
    }
    for (int index = 0; index < colCount; index++) {
        total += abs(cols[index] - colMedian);
    }

    free(rows);
    free(cols);
    return total;
}
