// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

#include <stdbool.h>
#include <stdlib.h>

static int distSq(int* a, int* b) {
    int dx = a[0] - b[0];
    int dy = a[1] - b[1];
    return dx * dx + dy * dy;
}

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

bool validSquare(int* p1, int p1Size, int* p2, int p2Size, int* p3, int p3Size, int* p4, int p4Size) {
    (void)p1Size;
    (void)p2Size;
    (void)p3Size;
    (void)p4Size;
    int* points[4] = {p1, p2, p3, p4};
    int distances[6];
    int idx = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            distances[idx++] = distSq(points[i], points[j]);
        }
    }
    qsort(distances, 6, sizeof(int), cmpInt);
    return distances[0] > 0
        && distances[0] == distances[1]
        && distances[1] == distances[2]
        && distances[2] == distances[3]
        && distances[4] == distances[5]
        && distances[4] == 2 * distances[0];
}
