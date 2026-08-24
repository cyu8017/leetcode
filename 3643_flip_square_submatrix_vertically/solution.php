<?php
// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution {
    function reverseSubmatrix($grid, $x, $y, $k) {
        for ($i = $x; $i < $x + intdiv($k, 2); $i++) {
            $i2 = $x + $k - 1 - ($i - $x);
            for ($j = $y; $j < $y + $k; $j++) {
                $tmp = $grid[$i][$j];
                $grid[$i][$j] = $grid[$i2][$j];
                $grid[$i2][$j] = $tmp;
            }
        }
        return $grid;
    }
}
