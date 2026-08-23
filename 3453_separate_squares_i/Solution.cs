// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

public class Solution {
    public double SeparateSquares(int[][] squares) {
        double OkArea(double y) {
            double below = 0;
            foreach (var sq in squares) {
                double yi = sq[1], l = sq[2];
                double top = yi + l;
                if (y <= yi) continue;
                if (y >= top) below += l * l;
                else below += l * (y - yi);
            }
            return below;
        }
        double total = 0;
        foreach (var sq in squares) {
            double l = sq[2];
            total += l * l;
        }
        double lo = 0.0, hi = 2e9;
        for (int it = 0; it < 60; it++) {
            double mid = (lo + hi) / 2;
            if (OkArea(mid) * 2 < total) lo = mid;
            else hi = mid;
        }
        return hi;
    }
}
