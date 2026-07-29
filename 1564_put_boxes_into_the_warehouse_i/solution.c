// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxBoxesInWarehouse(int* boxes, int boxesSize, int* warehouse, int warehouseSize) {
    for (int i = 1; i < warehouseSize; i++) {
        if (warehouse[i] > warehouse[i - 1]) warehouse[i] = warehouse[i - 1];
    }
    qsort(boxes, (size_t)boxesSize, sizeof(int), cmpInt);
    int room = warehouseSize - 1, used = 0;
    for (int i = 0; i < boxesSize; i++) {
        while (room >= 0 && warehouse[room] < boxes[i]) room--;
        if (room < 0) break;
        used++;
        room--;
    }
    return used;
}
