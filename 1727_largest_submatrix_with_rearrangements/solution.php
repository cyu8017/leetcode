<?php
// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function largestSubmatrix($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $heights = array_fill(0, $n, 0);
        $best = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $heights[$c] = $matrix[$r][$c] ? $heights[$c] + 1 : 0;
            }
            $sorted = $heights;
            rsort($sorted);
            for ($width = 1; $width <= $n; $width++) {
                $best = max($best, $width * $sorted[$width - 1]);
            }
        }
        return $best;
    }
}
