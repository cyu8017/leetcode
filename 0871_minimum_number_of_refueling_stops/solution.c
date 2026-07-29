// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

#include <stdlib.h>

int minRefuelStops(int target, int startFuel, int** stations, int stationsSize, int* stationsColSize) {
    (void)stationsColSize;
    int* heap = (int*)malloc((size_t)(stationsSize + 2) * sizeof(int));
    int hs = 0;
    int ans = 0, prev = 0, fuel = startFuel;
    for (int i = 0; i <= stationsSize; i++) {
        int pos = i < stationsSize ? stations[i][0] : target;
        int gas = i < stationsSize ? stations[i][1] : 0;
        fuel -= pos - prev;
        while (hs > 0 && fuel < 0) {
            fuel += heap[0];
            ans++;
            heap[0] = heap[--hs];
            int idx = 0;
            while (1) {
                int l = 2 * idx + 1, r = l + 1, largest = idx;
                if (l < hs && heap[l] > heap[largest]) largest = l;
                if (r < hs && heap[r] > heap[largest]) largest = r;
                if (largest == idx) break;
                int t = heap[idx]; heap[idx] = heap[largest]; heap[largest] = t;
                idx = largest;
            }
        }
        if (fuel < 0) { free(heap); return -1; }
        int idx = hs;
        heap[hs++] = gas;
        while (idx > 0) {
            int p = (idx - 1) / 2;
            if (heap[p] >= heap[idx]) break;
            int t = heap[p]; heap[p] = heap[idx]; heap[idx] = t;
            idx = p;
        }
        prev = pos;
    }
    free(heap);
    return ans;
}
