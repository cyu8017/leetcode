// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

#include <stdlib.h>

static int compareByUnitsDesc(const void* a, const void* b) {
    const int* boxA = *(int* const*)a;
    const int* boxB = *(int* const*)b;
    return boxB[1] - boxA[1];
}

int maximumUnits(int** boxTypes, int boxTypesSize, int* boxTypesColSize, int truckSize) {
    qsort(boxTypes, boxTypesSize, sizeof(int*), compareByUnitsDesc);
    int total = 0;
    for (int i = 0; i < boxTypesSize; i++) {
        int take = boxTypes[i][0] < truckSize ? boxTypes[i][0] : truckSize;
        total += take * boxTypes[i][1];
        truckSize -= take;
        if (truckSize == 0) {
            break;
        }
    }
    return total;
}
