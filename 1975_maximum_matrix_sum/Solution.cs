// LeetCode 1975 - Maximum Matrix Sum
// https://leetcode.com/problems/maximum-matrix-sum/

using System;

public class Solution {
    public long MaxMatrixSum(int[][] matrix) {
        long total = 0;
        int neg = 0, mn = int.MaxValue;
        foreach (var row in matrix) {
            foreach (int x in row) {
                if (x < 0) neg++;
                int ax = Math.Abs(x);
                total += ax;
                mn = Math.Min(mn, ax);
            }
        }
        return neg % 2 == 0 ? total : total - 2L * mn;
    }
}