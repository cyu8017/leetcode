// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

#include <stdlib.h>
#include <math.h>

typedef struct { double x, y; } Pt;

static double dist(Pt a, Pt b) {
    double dx = a.x - b.x, dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
}

static void circle2(Pt a, Pt b, Pt* c, double* r) {
    c->x = (a.x + b.x) / 2.0;
    c->y = (a.y + b.y) / 2.0;
    *r = dist(a, b) / 2.0;
}

static void circle3(Pt a, Pt b, Pt c0, Pt* c, double* r) {
    double ax = a.x, ay = a.y, bx = b.x, by = b.y, cx = c0.x, cy = c0.y;
    double d = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
    if (fabs(d) < 1e-12) {
        Pt c1, c2, c3; double r1, r2, r3;
        circle2(a, b, &c1, &r1);
        circle2(a, c0, &c2, &r2);
        circle2(b, c0, &c3, &r3);
        *c = c1; *r = r1;
        if (r2 < *r) { *c = c2; *r = r2; }
        if (r3 < *r) { *c = c3; *r = r3; }
        return;
    }
    c->x = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
    c->y = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
    *r = dist(*c, a);
}

static int inside(Pt c, double r, Pt p) {
    return dist(c, p) <= r + 1e-9;
}

double* outerTrees(int** trees, int treesSize, int* treesColSize, int* returnSize) {
    (void)treesColSize;
    Pt* pts = (Pt*)malloc((size_t)treesSize * sizeof(Pt));
    for (int i = 0; i < treesSize; i++) {
        pts[i].x = trees[i][0];
        pts[i].y = trees[i][1];
    }
    for (int i = treesSize - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        Pt t = pts[i]; pts[i] = pts[j]; pts[j] = t;
    }
    Pt center = pts[0];
    double radius = 0.0;
    int has = 0;
    for (int i = 0; i < treesSize; i++) {
        if (!has || !inside(center, radius, pts[i])) {
            center = pts[i];
            radius = 0.0;
            has = 1;
            for (int j = 0; j < i; j++) {
                if (!inside(center, radius, pts[j])) {
                    circle2(pts[i], pts[j], &center, &radius);
                    for (int k = 0; k < j; k++) {
                        if (!inside(center, radius, pts[k])) {
                            circle3(pts[i], pts[j], pts[k], &center, &radius);
                        }
                    }
                }
            }
        }
    }
    free(pts);
    double* res = (double*)malloc(3 * sizeof(double));
    res[0] = center.x;
    res[1] = center.y;
    res[2] = radius;
    *returnSize = 3;
    return res;
}
