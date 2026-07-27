// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

#include <stdlib.h>

typedef struct { int a, b, diff; } Cost;

static int cmp_cost(const void* x, const void* y) {
    return ((const Cost*)x)->diff - ((const Cost*)y)->diff;
}

int twoCitySchedCost(int** costs, int costsSize, int* costsColSize) {
    (void)costsColSize;
    Cost* arr = (Cost*)malloc((size_t)costsSize * sizeof(Cost));
    for (int i = 0; i < costsSize; i++) {
        arr[i].a = costs[i][0];
        arr[i].b = costs[i][1];
        arr[i].diff = costs[i][0] - costs[i][1];
    }
    qsort(arr, (size_t)costsSize, sizeof(Cost), cmp_cost);
    int n = costsSize / 2, sum = 0;
    for (int i = 0; i < n; i++) sum += arr[i].a;
    for (int i = n; i < costsSize; i++) sum += arr[i].b;
    free(arr);
    return sum;
}
