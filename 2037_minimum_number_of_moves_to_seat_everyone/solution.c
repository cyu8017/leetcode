// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    (void)studentsSize;
    qsort(seats, (size_t)seatsSize, sizeof(int), cmpInt);
    qsort(students, (size_t)seatsSize, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = 0; i < seatsSize; i++) {
        int d = seats[i] - students[i];
        if (d < 0) d = -d;
        ans += d;
    }
    return ans;
}
