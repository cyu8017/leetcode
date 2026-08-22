// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

#include <stdlib.h>

static int cmp_asc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

static int canPlace(int* arr, int n, int perim, int k, int mid) {
    for (int s = 0; s < n; s++) {
        int cnt = 1;
        int last = arr[s];
        int idx = s;
        while (cnt < k) {
            int target = last + mid;
            int found = 0;
            for (int step = 1; step < n; step++) {
                int ni = (idx + step) % n;
                int val = arr[ni];
                int add = (ni <= idx) ? perim : 0;
                if (val + add >= target) {
                    last = val + add;
                    idx = ni;
                    cnt++;
                    found = 1;
                    break;
                }
            }
            if (!found) break;
        }
        if (cnt == k && last - arr[s] <= perim - mid) return 1;
    }
    return 0;
}

int maxDistance(int side, int** points, int pointsSize, int* pointsColSize, int k) {
    (void)pointsColSize;
    int* arr = (int*)malloc((size_t)pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; i++) {
        int x = points[i][0], y = points[i][1];
        int d;
        if (y == 0) d = x;
        else if (x == side) d = side + y;
        else if (y == side) d = 2 * side + (side - x);
        else d = 3 * side + (side - y);
        arr[i] = d;
    }
    qsort(arr, (size_t)pointsSize, sizeof(int), cmp_asc);
    int perim = 4 * side;
    int lo = 0, hi = 2 * side;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (canPlace(arr, pointsSize, perim, k, mid)) lo = mid;
        else hi = mid - 1;
    }
    free(arr);
    return lo;
}
