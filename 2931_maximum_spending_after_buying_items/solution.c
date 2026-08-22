// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

#include <stdlib.h>

long long maxSpending(int** values, int valuesSize, int* valuesColSize) {
    int m = valuesSize, n = valuesColSize[0];
    int* idx = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) idx[i] = n - 1;
    long long ans = 0, day = 1;
    int total = m * n;
    for (int t = 0; t < total; t++) {
        int bestI = -1;
        long long bestV = 1LL << 60;
        for (int i = 0; i < m; i++) {
            if (idx[i] >= 0 && values[i][idx[i]] < bestV) {
                bestV = values[i][idx[i]];
                bestI = i;
            }
        }
        ans += bestV * day;
        idx[bestI]--;
        day++;
    }
    free(idx);
    return ans;
}
