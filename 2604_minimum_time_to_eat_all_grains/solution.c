// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static bool ok2604(int* hens, int hensSize, int* grains, int grainsSize, int t) {
    int j = 0;
    for (int hi = 0; hi < hensSize; hi++) {
        int h = hens[hi];
        if (j >= grainsSize) return true;
        if (grains[j] >= h) {
            while (j < grainsSize && grains[j] - h <= t) j++;
        } else {
            if (h - grains[j] > t) return false;
            int left = h - grains[j];
            int maxRight1 = t - 2 * left;
            int maxRight2 = (t - left) / 2;
            int reach = h;
            if (maxRight1 > maxRight2) {
                if (maxRight1 > 0) reach = h + maxRight1;
            } else {
                if (maxRight2 > 0) reach = h + maxRight2;
            }
            while (j < grainsSize && grains[j] <= reach) j++;
        }
    }
    return j >= grainsSize;
}

int minimumTime(int* hens, int hensSize, int* grains, int grainsSize) {
    qsort(hens, (size_t)hensSize, sizeof(int), cmpInt);
    qsort(grains, (size_t)grainsSize, sizeof(int), cmpInt);
    int lo = 0, hi = 2000000000;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (ok2604(hens, hensSize, grains, grainsSize, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
