// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxBoxesInWarehouse(int* boxes, int boxesSize, int* warehouse, int warehouseSize) {
    int n = warehouseSize;
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) left[i] = right[i] = warehouse[i];
    for (int i = 1; i < n; i++) if (left[i] > left[i - 1]) left[i] = left[i - 1];
    for (int i = n - 2; i >= 0; i--) if (right[i] > right[i + 1]) right[i] = right[i + 1];
    int* capacity = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) capacity[i] = left[i] > right[i] ? left[i] : right[i];
    qsort(capacity, (size_t)n, sizeof(int), cmpInt);
    qsort(boxes, (size_t)boxesSize, sizeof(int), cmpInt);
    int i = 0;
    for (int r = 0; r < n; r++) {
        if (i < boxesSize && boxes[i] <= capacity[r]) i++;
    }
    free(left); free(right); free(capacity);
    return i;
}
