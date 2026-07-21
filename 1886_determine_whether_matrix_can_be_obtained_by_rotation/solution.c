// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool equal(int** a, int** b, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] != b[i][j]) return false;
        }
    }
    return true;
}

bool findRotation(int** mat, int matSize, int* matColSize, int** target, int targetSize,
                  int* targetColSize) {
    (void)matColSize;
    (void)targetSize;
    (void)targetColSize;
    int n = matSize;
    int** current = (int**)malloc((size_t)n * sizeof(int*));
    int** next = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        current[i] = (int*)malloc((size_t)n * sizeof(int));
        next[i] = (int*)malloc((size_t)n * sizeof(int));
        memcpy(current[i], mat[i], (size_t)n * sizeof(int));
    }
    bool ok = false;
    for (int rot = 0; rot < 4; rot++) {
        if (equal(current, target, n)) {
            ok = true;
            break;
        }
        for (int col = 0; col < n; col++) {
            for (int row = 0; row < n; row++) {
                next[col][row] = current[n - 1 - row][col];
            }
        }
        for (int i = 0; i < n; i++) memcpy(current[i], next[i], (size_t)n * sizeof(int));
    }
    for (int i = 0; i < n; i++) {
        free(current[i]);
        free(next[i]);
    }
    free(current);
    free(next);
    return ok;
}
