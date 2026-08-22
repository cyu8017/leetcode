// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

#include <math.h>

double getMinDistSum(int** positions, int positionsSize, int* positionsColSize) {
    (void)positionsColSize;
    double x = 0, y = 0;
    for (int i = 0; i < positionsSize; i++) {
        x += positions[i][0];
        y += positions[i][1];
    }
    x /= positionsSize;
    y /= positionsSize;
    for (int iter = 0; iter < 10000; iter++) {
        double nx = 0, ny = 0, den = 0;
        int coincident = 0;
        double cx = 0, cy = 0;
        for (int i = 0; i < positionsSize; i++) {
            double px = positions[i][0], py = positions[i][1];
            double d = hypot(x - px, y - py);
            if (d < 1e-12) {
                coincident = 1;
                cx = px;
                cy = py;
                break;
            }
            nx += px / d;
            ny += py / d;
            den += 1.0 / d;
        }
        if (!coincident) {
            nx /= den;
            ny /= den;
        } else {
            nx = cx;
            ny = cy;
        }
        if (hypot(nx - x, ny - y) < 1e-8) {
            x = nx;
            y = ny;
            break;
        }
        x = nx;
        y = ny;
    }
    double dist = 0;
    for (int i = 0; i < positionsSize; i++) {
        dist += hypot(x - positions[i][0], y - positions[i][1]);
    }
    return dist;
}
