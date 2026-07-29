// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

int smallestCommonElement(int** mat, int matSize, int* matColSize) {
    (void)matColSize;
    if (matSize == 0) return -1;
    int cols = matColSize[0];
    char* present = (char*)calloc(10001, 1);
    for (int j = 0; j < cols; j++) present[mat[0][j]] = 1;
    for (int i = 1; i < matSize; i++) {
        char* next = (char*)calloc(10001, 1);
        for (int j = 0; j < matColSize[i]; j++) {
            int v = mat[i][j];
            if (present[v]) next[v] = 1;
        }
        free(present);
        present = next;
        int any = 0;
        for (int v = 0; v <= 10000; v++) {
            if (present[v]) {
                any = 1;
                break;
            }
        }
        if (!any) {
            free(present);
            return -1;
        }
    }
    int ans = INT_MAX;
    for (int v = 0; v <= 10000; v++) {
        if (present[v] && v < ans) ans = v;
    }
    free(present);
    return ans == INT_MAX ? -1 : ans;
}
