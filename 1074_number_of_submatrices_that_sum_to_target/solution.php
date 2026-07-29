<?php
// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @param Integer $target
     * @return Integer
     */
    function numSubmatrixSumTarget($matrix, $target) {
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $ans = 0;
        for ($left = 0; $left < $cols; $left++) {
            $rowSum = array_fill(0, $rows, 0);
            for ($right = $left; $right < $cols; $right++) {
                for ($r = 0; $r < $rows; $r++) {
                    $rowSum[$r] += $matrix[$r][$right];
                }
                $prefix = 0;
                $seen = [0 => 1];
                foreach ($rowSum as $val) {
                    $prefix += $val;
                    $ans += $seen[$prefix - $target] ?? 0;
                    $seen[$prefix] = ($seen[$prefix] ?? 0) + 1;
                }
            }
        }
        return $ans;
    }
}
