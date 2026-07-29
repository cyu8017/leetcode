<?php
// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function maxEqualRowsAfterFlips($matrix) {
        $patterns = [];
        foreach ($matrix as $row) {
            $base = $row[0];
            $keyParts = [];
            foreach ($row as $x) {
                $keyParts[] = $x ^ $base;
            }
            $key = implode(",", $keyParts);
            $patterns[$key] = ($patterns[$key] ?? 0) + 1;
        }
        return max($patterns);
    }
}
