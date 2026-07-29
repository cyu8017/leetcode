// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int eliminateMaximum(int* dist, int distSize, int* speed, int speedSize) {
    (void)speedSize;
    int* arrival = (int*)malloc((size_t)distSize * sizeof(int));
    for (int i = 0; i < distSize; i++) {
        arrival[i] = (dist[i] + speed[i] - 1) / speed[i];
    }
    qsort(arrival, (size_t)distSize, sizeof(int), cmpInt);
    for (int i = 0; i < distSize; i++) {
        if (arrival[i] <= i) {
            free(arrival);
            return i;
        }
    }
    free(arrival);
    return distSize;
}
