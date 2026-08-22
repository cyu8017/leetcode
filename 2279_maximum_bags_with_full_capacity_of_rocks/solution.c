// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maximumBags(int* capacity, int capacitySize, int* rocks, int rocksSize, int additionalRocks) {
    (void)rocksSize;
    int* need = (int*)malloc((size_t)capacitySize * sizeof(int));
    for (int i = 0; i < capacitySize; i++) {
        need[i] = capacity[i] - rocks[i];
    }
    qsort(need, (size_t)capacitySize, sizeof(int), cmp_int);
    int ans = 0;
    for (int i = 0; i < capacitySize; i++) {
        if (additionalRocks < need[i]) break;
        additionalRocks -= need[i];
        ans++;
    }
    free(need);
    return ans;
}
