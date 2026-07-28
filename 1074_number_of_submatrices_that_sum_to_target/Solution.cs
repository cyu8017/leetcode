// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

using System.Collections.Generic;

public class Solution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) {
        int rows = matrix.Length, cols = matrix[0].Length;
        int ans = 0;
        for (int left = 0; left < cols; left++) {
            int[] rowSum = new int[rows];
            for (int right = left; right < cols; right++) {
                for (int r = 0; r < rows; r++) {
                    rowSum[r] += matrix[r][right];
                }
                int prefix = 0;
                var seen = new Dictionary<int, int> { [0] = 1 };
                foreach (int val in rowSum) {
                    prefix += val;
                    ans += seen.GetValueOrDefault(prefix - target);
                    seen[prefix] = seen.GetValueOrDefault(prefix) + 1;
                }
            }
        }
        return ans;
    }
}
