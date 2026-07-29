// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

#include <stdlib.h>

int minTaps(int n, int* ranges, int rangesSize) {
    (void)rangesSize;
    int* farthest = (int*)calloc(n + 1, sizeof(int));
    for (int center = 0; center <= n; center++) {
        int left = center - ranges[center]; if (left < 0) left = 0;
        int right = center + ranges[center]; if (right > n) right = n;
        if (right > farthest[left]) farthest[left] = right;
    }
    int taps = 0, end = 0, reach = 0;
    for (int position = 0; position < n; position++) {
        if (farthest[position] > reach) reach = farthest[position];
        if (position == end) {
            if (reach <= position) { free(farthest); return -1; }
            taps++;
            end = reach;
        }
    }
    free(farthest);
    return taps;
}
