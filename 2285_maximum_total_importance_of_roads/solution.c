// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maximumImportance(int n, int** roads, int roadsSize, int* roadsColSize) {
    (void)roadsColSize;
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < roadsSize; i++) {
        deg[roads[i][0]]++;
        deg[roads[i][1]]++;
    }
    qsort(deg, (size_t)n, sizeof(int), cmp_int);
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        ans += (long long)deg[i] * (i + 1);
    }
    free(deg);
    return ans;
}
