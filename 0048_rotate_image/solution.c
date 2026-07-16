// LeetCode 0048 - Rotate Image
// https://leetcode.com/problems/rotate-image/

static void swap_int(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    for (int i = 0; i < matrixSize; i++) {
        for (int j = i + 1; j < matrixSize; j++) {
            swap_int(&matrix[i][j], &matrix[j][i]);
        }
    }

    for (int i = 0; i < matrixSize; i++) {
        int left = 0;
        int right = matrixColSize[i] - 1;
        while (left < right) {
            swap_int(&matrix[i][left], &matrix[i][right]);
            left++;
            right--;
        }
    }
}
