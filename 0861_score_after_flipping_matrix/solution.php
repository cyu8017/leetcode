<?php
// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function matrixScore($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        for ($i = 0; $i < $m; $i++) {
            if ($grid[$i][0] === 0) {
                for ($j = 0; $j < $n; $j++) $grid[$i][$j] ^= 1;
            }
        }
        $ans = $m * (1 << ($n - 1));
        for ($j = 1; $j < $n; $j++) {
            $ones = 0;
            for ($i = 0; $i < $m; $i++) $ones += $grid[$i][$j];
            $ans += max($ones, $m - $ones) * (1 << ($n - 1 - $j));
        }
        return $ans;
    }
}
