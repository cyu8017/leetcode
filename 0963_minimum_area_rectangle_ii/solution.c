// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

#include <stdlib.h>
#include <math.h>
#include <float.h>

double minAreaFreeRect(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    double ans = DBL_MAX;
    for (int i = 0; i < pointsSize; i++) {
        for (int j = i + 1; j < pointsSize; j++) {
            for (int k = j + 1; k < pointsSize; k++) {
                double x1 = points[i][0], y1 = points[i][1];
                double x2 = points[j][0], y2 = points[j][1];
                double x3 = points[k][0], y3 = points[k][1];
                // try each as corner
                double pts[3][2] = {{x1,y1},{x2,y2},{x3,y3}};
                for (int c = 0; c < 3; c++) {
                    double cx = pts[c][0], cy = pts[c][1];
                    double ax = pts[(c+1)%3][0] - cx, ay = pts[(c+1)%3][1] - cy;
                    double bx = pts[(c+2)%3][0] - cx, by = pts[(c+2)%3][1] - cy;
                    if (fabs(ax * bx + ay * by) > 1e-9) continue;
                    double dx = cx + ax + bx, dy = cy + ay + by;
                    int found = 0;
                    for (int t = 0; t < pointsSize; t++) {
                        if (fabs(points[t][0] - dx) < 1e-9 && fabs(points[t][1] - dy) < 1e-9) { found = 1; break; }
                    }
                    if (!found) continue;
                    double area = sqrt(ax*ax+ay*ay) * sqrt(bx*bx+by*by);
                    if (area > 0 && area < ans) ans = area;
                }
            }
        }
    }
    return ans == DBL_MAX ? 0.0 : ans;
}
