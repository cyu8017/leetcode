// LeetCode 2332 - The Latest Time to Catch a Bus
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int latestTimeCatchTheBus(int* buses, int busesSize, int* passengers, int passengersSize, int capacity) {
    qsort(buses, (size_t)busesSize, sizeof(int), cmpInt);
    qsort(passengers, (size_t)passengersSize, sizeof(int), cmpInt);
    int pos = 0;
    for (int bi = 0; bi < busesSize; bi++) {
        int bus = buses[bi];
        int cap = capacity;
        while (cap > 0 && pos < passengersSize && passengers[pos] <= bus) {
            pos++;
            cap--;
        }
        if (bi == busesSize - 1) {
            int cand = bus;
            if (cap == 0) cand = passengers[pos - 1];
            for (;;) {
                int lo = 0, hi = passengersSize;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (passengers[mid] < cand) lo = mid + 1;
                    else hi = mid;
                }
                if (lo < passengersSize && passengers[lo] == cand) cand--;
                else break;
            }
            return cand;
        }
    }
    return -1;
}
