<?php
// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

class Solution {
    /**
     * @param String[][] $matrix
     * @return Integer
     */
    function maximalSquare($matrix) {
        if ($matrix === null || count($matrix) === 0) {
            return 0;
        }
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $dp = array_fill(0, $cols + 1, 0);
        $maxSide = 0;
        $prev = 0;
        for ($row = 1; $row <= $rows; $row++) {
            for ($col = 1; $col <= $cols; $col++) {
                $temp = $dp[$col];
                if ($matrix[$row - 1][$col - 1] === "1") {
                    $dp[$col] = min($dp[$col], $dp[$col - 1], $prev) + 1;
                    $maxSide = max($maxSide, $dp[$col]);
                } else {
                    $dp[$col] = 0;
                }
                $prev = $temp;
            }
        }
        return $maxSide * $maxSide;
    }
}
