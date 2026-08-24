<?php
// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

class Solution {
    /**
     * @param Integer $n
     * @return Integer[][]
     */
    function generateMatrix($n) {
        $matrix = array_fill(0, $n, array_fill(0, $n, 0));
        $top = 0;
        $bottom = $n - 1;
        $left = 0;
        $right = $n - 1;
        $num = 1;

        while ($top <= $bottom && $left <= $right) {
            for ($col = $left; $col <= $right; $col++) {
                $matrix[$top][$col] = $num++;
            }
            $top++;

            for ($row = $top; $row <= $bottom; $row++) {
                $matrix[$row][$right] = $num++;
            }
            $right--;

            if ($top <= $bottom) {
                for ($col = $right; $col >= $left; $col--) {
                    $matrix[$bottom][$col] = $num++;
                }
                $bottom--;
            }

            if ($left <= $right) {
                for ($row = $bottom; $row >= $top; $row--) {
                    $matrix[$row][$left] = $num++;
                }
                $left++;
            }
        }

        return $matrix;
    }
}
