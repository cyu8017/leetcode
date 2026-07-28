// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        Map<String, Integer> patterns = new HashMap<>();
        int best = 0;
        for (int[] row : matrix) {
            int base = row[0];
            StringBuilder buf = new StringBuilder();
            for (int x : row) {
                buf.append(x ^ base);
            }
            String key = buf.toString();
            int count = patterns.merge(key, 1, Integer::sum);
            best = Math.max(best, count);
        }
        return best;
    }
}
