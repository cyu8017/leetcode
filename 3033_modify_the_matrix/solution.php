<?php
// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

class Solution {
    function modifiedMatrix($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        for ($j = 0; $j < $n; $j++) {
            $mx = -1;
            for ($i = 0; $i < $m; $i++) $mx = max($mx, $matrix[$i][$j]);
            for ($i = 0; $i < $m; $i++) if ($matrix[$i][$j] === -1) $matrix[$i][$j] = $mx;
        }
        return $matrix;
    }
}
