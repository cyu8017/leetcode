// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

#include <stdlib.h>
#include <string.h>

int* corpFlightBookings(int** bookings, int bookingsSize, int* bookingsColSize, int n, int* returnSize) {
    (void)bookingsColSize;
    int* diff = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < bookingsSize; i++) {
        diff[bookings[i][0] - 1] += bookings[i][2];
        diff[bookings[i][1]] -= bookings[i][2];
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int cur = 0;
    for (int i = 0; i < n; i++) {
        cur += diff[i];
        ans[i] = cur;
    }
    free(diff);
    *returnSize = n;
    return ans;
}
