// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[] row = new double[] {(double) poured};
        for (int r = 0; r < query_row; r++) {
            double[] nextRow = new double[r + 2];
            for (int i = 0; i < row.length; i++) {
                double overflow = (row[i] - 1.0) / 2.0;
                if (overflow > 0) {
                    nextRow[i] += overflow;
                    nextRow[i + 1] += overflow;
                }
            }
            row = nextRow;
        }
        return Math.min(1.0, row[query_glass]);
    }
}
