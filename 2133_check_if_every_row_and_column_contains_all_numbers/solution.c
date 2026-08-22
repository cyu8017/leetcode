// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool checkValid(int** matrix, int matrixSize, int* matrixColSize) {
    (void)matrixColSize;
    int n = matrixSize;
    for (int i = 0; i < n; i++) {
        bool* row = (bool*)calloc((size_t)n + 1, sizeof(bool));
        bool* col = (bool*)calloc((size_t)n + 1, sizeof(bool));
        for (int j = 0; j < n; j++) {
            if (row[matrix[i][j]] || col[matrix[j][i]]) {
                free(row); free(col);
                return false;
            }
            row[matrix[i][j]] = true;
            col[matrix[j][i]] = true;
        }
        free(row); free(col);
    }
    return true;
}
