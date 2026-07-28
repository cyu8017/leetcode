// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int rows = matrix.length, cols = matrix[0].length;
        int ans = 0;
        for (int left = 0; left < cols; left++) {
            int[] rowSum = new int[rows];
            for (int right = left; right < cols; right++) {
                for (int r = 0; r < rows; r++) {
                    rowSum[r] += matrix[r][right];
                }
                int prefix = 0;
                Map<Integer, Integer> seen = new HashMap<>();
                seen.put(0, 1);
                for (int val : rowSum) {
                    prefix += val;
                    ans += seen.getOrDefault(prefix - target, 0);
                    seen.merge(prefix, 1, Integer::sum);
                }
            }
        }
        return ans;
    }
}
