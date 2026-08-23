// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

class Solution {
    public double separateSquares(int[][] squares) {
        double total = 0;
        for (int[] sq : squares) {
            double l = sq[2];
            total += l * l;
        }
        double lo = 0.0, hi = 2e9;
        for (int it = 0; it < 60; it++) {
            double mid = (lo + hi) / 2;
            if (okArea(squares, mid) * 2 < total) lo = mid;
            else hi = mid;
        }
        return hi;
    }

    private double okArea(int[][] squares, double y) {
        double below = 0;
        for (int[] sq : squares) {
            double yi = sq[1], l = sq[2];
            double top = yi + l;
            if (y <= yi) continue;
            if (y >= top) below += l * l;
            else below += l * (y - yi);
        }
        return below;
    }
}
