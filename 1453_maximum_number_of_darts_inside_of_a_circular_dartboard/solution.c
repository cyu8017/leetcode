// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

#include <math.h>

int numPoints(int** darts, int dartsSize, int* dartsColSize, int r) {
    (void)dartsColSize;
    int ans = dartsSize ? 1 : 0;
    double rr = (double)r * r;
    for (int i = 0; i < dartsSize; i++) {
        for (int j = i + 1; j < dartsSize; j++) {
            double x1 = darts[i][0], y1 = darts[i][1];
            double x2 = darts[j][0], y2 = darts[j][1];
            double dx = x2 - x1, dy = y2 - y1;
            double d2 = dx * dx + dy * dy;
            if (d2 > 4 * rr || d2 == 0) continue;
            double d = sqrt(d2);
            double h = sqrt(rr - d2 / 4);
            double mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
            for (int sign = -1; sign <= 1; sign += 2) {
                double cx = mx + sign * (-dy) * h / d;
                double cy = my + sign * dx * h / d;
                int count = 0;
                for (int t = 0; t < dartsSize; t++) {
                    double ex = darts[t][0] - cx, ey = darts[t][1] - cy;
                    if (ex * ex + ey * ey <= rr + 1e-7) count++;
                }
                if (count > ans) ans = count;
            }
        }
    }
    return ans;
}
