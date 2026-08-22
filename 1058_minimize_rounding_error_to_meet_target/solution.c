// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int cmpDoubleDesc(const void* a, const void* b) {
    double da = *(const double*)a;
    double db = *(const double*)b;
    if (da < db) {
        return 1;
    }
    if (da > db) {
        return -1;
    }
    return 0;
}

char* minimizeError(char** prices, int pricesSize, int target) {
    int floors = 0;
    double* fracs = (double*)malloc((size_t)pricesSize * sizeof(double));
    int fracCount = 0;
    for (int i = 0; i < pricesSize; i++) {
        double value = atof(prices[i]);
        int floorVal = (int)value;
        floors += floorVal;
        double frac = value - floorVal;
        if (frac > 1e-9) {
            fracs[fracCount++] = frac;
        }
    }
    int ceilCount = target - floors;
    if (ceilCount < 0 || ceilCount > fracCount) {
        free(fracs);
        char* bad = (char*)malloc(3);
        strcpy(bad, "-1");
        return bad;
    }
    qsort(fracs, (size_t)fracCount, sizeof(double), cmpDoubleDesc);
    double error = 0.0;
    for (int i = 0; i < ceilCount; i++) {
        error += 1.0 - fracs[i];
    }
    for (int i = ceilCount; i < fracCount; i++) {
        error += fracs[i];
    }
    free(fracs);
    char* ans = (char*)malloc(32);
    sprintf(ans, "%.3f", error);
    return ans;
}
