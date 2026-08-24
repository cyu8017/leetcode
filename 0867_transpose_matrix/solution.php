<?php
// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function transpose($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $ans = array_fill(0, $n, array_fill(0, $m, 0));
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++) $ans[$j][$i] = $matrix[$i][$j];
        return $ans;
    }
}
