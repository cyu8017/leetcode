// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

#include <stdlib.h>

long long maxEnergyBoost(int* energyDrinkA, int energyDrinkASize, int* energyDrinkB, int energyDrinkBSize) {
    (void)energyDrinkBSize;
    int n = energyDrinkASize;
    long long *dpA = (long long*)malloc((size_t)n * sizeof(long long));
    long long *dpB = (long long*)malloc((size_t)n * sizeof(long long));
    dpA[0] = energyDrinkA[0];
    dpB[0] = energyDrinkB[0];
    if (n == 1) {
        long long ans = dpA[0] > dpB[0] ? dpA[0] : dpB[0];
        free(dpA); free(dpB);
        return ans;
    }
    dpA[1] = (long long)energyDrinkA[1] + dpA[0];
    dpB[1] = (long long)energyDrinkB[1] + dpB[0];
    for (int i = 2; i < n; i++) {
        long long x = dpA[i - 1];
        if (dpB[i - 2] > x) x = dpB[i - 2];
        dpA[i] = energyDrinkA[i] + x;
        long long y = dpB[i - 1];
        if (dpA[i - 2] > y) y = dpA[i - 2];
        dpB[i] = energyDrinkB[i] + y;
    }
    long long ans = dpA[n - 1] > dpB[n - 1] ? dpA[n - 1] : dpB[n - 1];
    free(dpA); free(dpB);
    return ans;
}
