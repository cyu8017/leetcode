// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

import java.util.*;

class Solution {
    public double[] outerTrees(int[][] trees) {
        List<double[]> pts = new ArrayList<>();
        for (int[] t : trees) pts.add(new double[]{t[0], t[1]});
        Collections.shuffle(pts);
        double[] circle = null; // cx, cy, r
        for (int i = 0; i < pts.size(); i++) {
            double[] p = pts.get(i);
            if (circle == null || !inside(circle, p)) {
                circle = new double[]{p[0], p[1], 0};
                for (int j = 0; j < i; j++) {
                    double[] q = pts.get(j);
                    if (!inside(circle, q)) {
                        circle = circle2(p, q);
                        for (int k = 0; k < j; k++) {
                            double[] r = pts.get(k);
                            if (!inside(circle, r)) circle = circle3(p, q, r);
                        }
                    }
                }
            }
        }
        return new double[]{circle[0], circle[1], circle[2]};
    }

    private boolean inside(double[] cir, double[] p) {
        return dist(new double[]{cir[0], cir[1]}, p) <= cir[2] + 1e-9;
    }

    private double dist(double[] a, double[] b) {
        double dx = a[0] - b[0], dy = a[1] - b[1];
        return Math.sqrt(dx * dx + dy * dy);
    }

    private double[] circle2(double[] a, double[] b) {
        double cx = (a[0] + b[0]) / 2, cy = (a[1] + b[1]) / 2;
        return new double[]{cx, cy, dist(a, b) / 2};
    }

    private double[] circle3(double[] a, double[] b, double[] c) {
        double ax = a[0], ay = a[1], bx = b[0], by = b[1], cx = c[0], cy = c[1];
        double d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
        if (Math.abs(d) < 1e-12) {
            double[] c1 = circle2(a, b), c2 = circle2(a, c), c3 = circle2(b, c);
            if (c1[2] <= c2[2] && c1[2] <= c3[2]) return c1;
            if (c2[2] <= c3[2]) return c2;
            return c3;
        }
        double ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
        double uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
        double[] center = new double[]{ux, uy};
        return new double[]{ux, uy, dist(center, a)};
    }
}
