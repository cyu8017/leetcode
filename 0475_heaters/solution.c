// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int absInt(int value) {
    return value < 0 ? -value : value;
}

int findRadius(int* houses, int housesSize, int* heaters, int heatersSize) {
    qsort(heaters, (size_t)heatersSize, sizeof(int), cmpInt);
    int radius = 0;
    for (int i = 0; i < housesSize; i++) {
        int house = houses[i];
        int low = 0;
        int high = heatersSize;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (heaters[mid] < house) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        int best = 2147483647;
        if (low < heatersSize) {
            int d = absInt(heaters[low] - house);
            if (d < best) {
                best = d;
            }
        }
        if (low > 0) {
            int d = absInt(heaters[low - 1] - house);
            if (d < best) {
                best = d;
            }
        }
        if (best > radius) {
            radius = best;
        }
    }
    return radius;
}
