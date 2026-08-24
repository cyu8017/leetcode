<?php
// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution {
    function onesMinusZeros($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $row = array_fill(0, $m, 0);
        $col = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $row[$i] += $grid[$i][$j];
                $col[$j] += $grid[$i][$j];
            }
        }
        $ans = [];
        for ($i = 0; $i < $m; $i++) {
            $ans[$i] = array_fill(0, $n, 0);
            for ($j = 0; $j < $n; $j++) {
                $ans[$i][$j] = $row[$i] + $col[$j] - ($m - $row[$i]) - ($n - $col[$j]);
            }
        }
        return $ans;
    }
}
