// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

#include <stdlib.h>
#include <math.h>

double largestTriangleArea(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    double best = 0.0;
    for (int i = 0; i < pointsSize; i++) {
        int x1 = points[i][0], y1 = points[i][1];
        for (int j = i + 1; j < pointsSize; j++) {
            int x2 = points[j][0], y2 = points[j][1];
            for (int k = j + 1; k < pointsSize; k++) {
                int x3 = points[k][0], y3 = points[k][1];
                double area = fabs((double)x1 * (y2 - y3) + (double)x2 * (y3 - y1) +
                                   (double)x3 * (y1 - y2)) /
                              2.0;
                if (area > best) best = area;
            }
        }
    }
    return best;
}
