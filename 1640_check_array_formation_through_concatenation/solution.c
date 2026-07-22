// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

#include <stdbool.h>
#include <stdlib.h>

bool canFormArray(int* arr, int arrSize, int** pieces, int piecesSize, int* piecesColSize) {
    int* byFirst = (int*)malloc(101 * sizeof(int));
    for (int i = 0; i <= 100; i++) byFirst[i] = -1;
    for (int i = 0; i < piecesSize; i++) byFirst[pieces[i][0]] = i;
    int i = 0;
    while (i < arrSize) {
        int idx = byFirst[arr[i]];
        if (idx < 0) { free(byFirst); return false; }
        for (int j = 0; j < piecesColSize[idx]; j++) {
            if (i >= arrSize || arr[i] != pieces[idx][j]) { free(byFirst); return false; }
            i++;
        }
    }
    free(byFirst);
    return true;
}
