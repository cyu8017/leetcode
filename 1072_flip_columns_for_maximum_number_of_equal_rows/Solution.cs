// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

using System.Collections.Generic;

public class Solution {
    public int MaxEqualRowsAfterFlips(int[][] matrix) {
        var patterns = new Dictionary<string, int>();
        int best = 0;
        foreach (var row in matrix) {
            int bas = row[0];
            char[] key = new char[row.Length];
            for (int i = 0; i < row.Length; i++) {
                key[i] = (char)('0' + (row[i] ^ bas));
            }
            string k = new string(key);
            patterns[k] = patterns.GetValueOrDefault(k) + 1;
            if (patterns[k] > best) {
                best = patterns[k];
            }
        }
        return best;
    }
}
