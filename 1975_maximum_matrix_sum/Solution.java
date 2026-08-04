// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

class Solution {
    public long maxMatrixSum(int[][] matrix) {
        long total = 0;
        int neg = 0, mn = Integer.MAX_VALUE;
        for (int[] row : matrix) {
            for (int x : row) {
                if (x < 0) neg++;
                int ax = Math.abs(x);
                total += ax;
                mn = Math.min(mn, ax);
            }
        }
        return neg % 2 == 0 ? total : total - 2L * mn;
    }
}
