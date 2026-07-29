// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxDistance(int* position, int positionSize, int m) {
    qsort(position, (size_t)positionSize, sizeof(int), cmpInt);
    int lo = 1, hi = (position[positionSize - 1] - position[0]) / (m - 1);
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int count = 1, last = position[0];
        for (int i = 1; i < positionSize; i++) {
            if (position[i] - last >= mid) {
                count++;
                last = position[i];
            }
        }
        if (count >= m) lo = mid + 1;
        else hi = mid - 1;
    }
    return hi;
}
