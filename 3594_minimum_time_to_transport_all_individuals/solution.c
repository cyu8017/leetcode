// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

double minTime(int n, int k, int m, int* time, int timeSize, double* mul, int mulSize) {
    (void)timeSize; (void)mulSize;
    int* t = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) t[i] = time[i];
    qsort(t, (size_t)n, sizeof(int), cmp_int);
    double total = 0; int stage = 0, left = n;
    while (left > 0) {
        int take = k < left ? k : left;
        int slow = t[left - 1];
        total += (double)slow * mul[stage % m];
        left -= take; stage++;
        if (left > 0) { total += (double)t[0] * mul[stage % m]; stage++; }
    }
    free(t);
    return total;
}
