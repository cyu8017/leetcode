// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

#include <stdlib.h>

int maxNumberOfFamilies(int n, int** reservedSeats, int reservedSeatsSize, int* reservedSeatsColSize) {
    (void)reservedSeatsColSize;
    // map row -> mask using simple array of pairs
    typedef struct { int row, mask; } RM;
    RM* rows = (RM*)malloc(reservedSeatsSize * sizeof(RM));
    int rn = 0;
    for (int i = 0; i < reservedSeatsSize; i++) {
        int r = reservedSeats[i][0], c = reservedSeats[i][1];
        if (c < 2 || c > 9) continue;
        int found = -1;
        for (int j = 0; j < rn; j++) if (rows[j].row == r) { found = j; break; }
        if (found < 0) { rows[rn].row = r; rows[rn].mask = 0; found = rn++; }
        rows[found].mask |= 1 << (c - 2);
    }
    int ans = 2 * (n - rn);
    for (int i = 0; i < rn; i++) {
        int m = rows[i].mask;
        int left = (m & 0x0F) == 0;
        int right = (m & 0xF0) == 0;
        int middle = (m & 0x3C) == 0;
        if (left && right) ans += 2;
        else if (left || right || middle) ans += 1;
    }
    free(rows);
    return ans;
}
