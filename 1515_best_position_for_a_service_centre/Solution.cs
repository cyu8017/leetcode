// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

using System;

public class Solution {
    public double GetMinDistSum(int[][] positions) {
        double x = 0, y = 0;
        foreach (var p in positions) { x += p[0]; y += p[1]; }
        x /= positions.Length;
        y /= positions.Length;

        double Hypot(double a, double b) => Math.Sqrt(a * a + b * b);

        double Dist(double a, double b) {
            double sum = 0;
            foreach (var p in positions) sum += Hypot(a - p[0], b - p[1]);
            return sum;
        }

        for (int iter = 0; iter < 10000; iter++) {
            double numeratorX = 0, numeratorY = 0, denominator = 0;
            bool coincident = false;
            double cx = 0, cy = 0;
            foreach (var p in positions) {
                double d = Hypot(x - p[0], y - p[1]);
                if (d < 1e-12) {
                    coincident = true;
                    cx = p[0];
                    cy = p[1];
                    break;
                }
                numeratorX += p[0] / d;
                numeratorY += p[1] / d;
                denominator += 1 / d;
            }
            double nx = coincident ? cx : numeratorX / denominator;
            double ny = coincident ? cy : numeratorY / denominator;
            if (Hypot(nx - x, ny - y) < 1e-8) {
                x = nx; y = ny;
                break;
            }
            x = nx; y = ny;
        }
        return Dist(x, y);
    }
}
