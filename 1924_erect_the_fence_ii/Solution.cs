// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public double[] OuterTrees(int[][] trees) {
        var pts = new List<(double x, double y)>();
        foreach (var t in trees) pts.Add((t[0], t[1]));
        var rng = new Random(0);
        for (int i = pts.Count - 1; i > 0; i--) {
            int j = rng.Next(i + 1);
            (pts[i], pts[j]) = (pts[j], pts[i]);
        }

        double Dist((double x, double y) a, (double x, double y) b) =>
            Math.Sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));

        ((double x, double y) c, double r) Circle2((double x, double y) a, (double x, double y) b) {
            var c = ((a.x + b.x) / 2, (a.y + b.y) / 2);
            return (c, Dist(a, b) / 2);
        }

        ((double x, double y) c, double r) Circle3((double x, double y) a, (double x, double y) b, (double x, double y) c) {
            double ax = a.x, ay = a.y, bx = b.x, by = b.y, cx = c.x, cy = c.y;
            double d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
            if (Math.Abs(d) < 1e-12) {
                var cands = new[] { Circle2(a, b), Circle2(a, c), Circle2(b, c) };
                ((double x, double y) c, double r) best = cands[0];
                foreach (var cand in cands) if (cand.r < best.r) best = cand;
                return best;
            }
            double ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
            double uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
            var center = (ux, uy);
            return (center, Dist(center, a));
        }

        bool Inside(((double x, double y) c, double r)? cir, (double x, double y) p) {
            if (cir == null) return false;
            return Dist(cir.Value.c, p) <= cir.Value.r + 1e-9;
        }

        ((double x, double y) c, double r)? circle = null;
        for (int i = 0; i < pts.Count; i++) {
            var p = pts[i];
            if (circle == null || !Inside(circle, p)) {
                circle = (p, 0.0);
                for (int j = 0; j < i; j++) {
                    var q = pts[j];
                    if (!Inside(circle, q)) {
                        circle = Circle2(p, q);
                        for (int k = 0; k < j; k++) {
                            var r = pts[k];
                            if (!Inside(circle, r)) circle = Circle3(p, q, r);
                        }
                    }
                }
            }
        }
        return new double[] { circle.Value.c.x, circle.Value.c.y, circle.Value.r };
    }
}