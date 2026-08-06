<?php
// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function countSquares($matrix) {
        $answer = 0;
        $m = count($matrix);
        $n = count($matrix[0]);
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($matrix[$r][$c] && $r && $c) {
                    $matrix[$r][$c] += min($matrix[$r - 1][$c], $matrix[$r][$c - 1], $matrix[$r - 1][$c - 1]);
                }
                $answer += $matrix[$r][$c];
            }
        }
        return $answer;
    }
}
