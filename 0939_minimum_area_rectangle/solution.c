// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

#include <stdlib.h>
#include <limits.h>

int minAreaRect(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    int cap = 1;
    while (cap < pointsSize * 4) cap <<= 1;
    long long* table = (long long*)malloc((size_t)cap * sizeof(long long));
    for (int i = 0; i < cap; i++) table[i] = LLONG_MIN;
    for (int i = 0; i < pointsSize; i++) {
        long long k = ((long long)points[i][0] << 20) | (unsigned)points[i][1];
        unsigned h = (unsigned)((k * 2654435761ULL) & (cap - 1));
        while (table[h] != LLONG_MIN) h = (h + 1) & (cap - 1);
        table[h] = k;
    }
    int ans = INT_MAX;
    for (int i = 0; i < pointsSize; i++) {
        for (int j = i + 1; j < pointsSize; j++) {
            int x1 = points[i][0], y1 = points[i][1];
            int x2 = points[j][0], y2 = points[j][1];
            if (x1 == x2 || y1 == y2) continue;
            long long k1 = ((long long)x1 << 20) | (unsigned)y2;
            long long k2 = ((long long)x2 << 20) | (unsigned)y1;
            int ok1 = 0, ok2 = 0;
            unsigned h = (unsigned)((k1 * 2654435761ULL) & (cap - 1));
            while (table[h] != LLONG_MIN) { if (table[h] == k1) { ok1 = 1; break; } h = (h + 1) & (cap - 1); }
            h = (unsigned)((k2 * 2654435761ULL) & (cap - 1));
            while (table[h] != LLONG_MIN) { if (table[h] == k2) { ok2 = 1; break; } h = (h + 1) & (cap - 1); }
            if (ok1 && ok2) {
                int area = abs(x1 - x2) * abs(y1 - y2);
                if (area < ans) ans = area;
            }
        }
    }
    free(table);
    return ans == INT_MAX ? 0 : ans;
}
