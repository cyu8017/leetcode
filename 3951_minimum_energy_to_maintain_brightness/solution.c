// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

#include <stdlib.h>

static int cmpIntv3951(const void* a, const void* b) {
    const int* x = *(const int* const*)a;
    const int* y = *(const int* const*)b;
    return x[0] - y[0];
}

long long minEnergy(int n, int brightness, int** intervals, int intervalsSize, int* intervalsColSize) {
    (void)n; (void)intervalsColSize;
    int** sorted = malloc((size_t)intervalsSize * sizeof(int*));
    for (int i = 0; i < intervalsSize; i++) sorted[i] = intervals[i];
    qsort(sorted, (size_t)intervalsSize, sizeof(int*), cmpIntv3951);
    int* ms = malloc((size_t)intervalsSize * sizeof(int));
    int* me = malloc((size_t)intervalsSize * sizeof(int));
    int mn = 0;
    ms[0] = sorted[0][0]; me[0] = sorted[0][1]; mn = 1;
    for (int i = 1; i < intervalsSize; i++) {
        if (me[mn - 1] < sorted[i][0]) {
            ms[mn] = sorted[i][0]; me[mn] = sorted[i][1]; mn++;
        } else if (sorted[i][1] > me[mn - 1]) me[mn - 1] = sorted[i][1];
    }
    long long ans = 0;
    for (int i = 0; i < mn; i++) {
        long long m = me[i] - ms[i] + 1;
        ans += (long long)((brightness + 2) / 3) * m;
    }
    free(sorted); free(ms); free(me);
    return ans;
}
