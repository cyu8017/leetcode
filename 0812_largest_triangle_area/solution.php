<?php
// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

class Solution {
    /**
     * @param Integer[][] $points
     * @return Float
     */
    function largestTriangleArea($points) {
        $best = 0.0;
        $n = count($points);
        for ($i = 0; $i < $n; $i++) {
            $x1 = $points[$i][0];
            $y1 = $points[$i][1];
            for ($j = $i + 1; $j < $n; $j++) {
                $x2 = $points[$j][0];
                $y2 = $points[$j][1];
                for ($k = $j + 1; $k < $n; $k++) {
                    $x3 = $points[$k][0];
                    $y3 = $points[$k][1];
                    $area = abs($x1 * ($y2 - $y3) + $x2 * ($y3 - $y1) + $x3 * ($y1 - $y2)) / 2.0;
                    $best = max($best, $area);
                }
            }
        }
        return $best;
    }
}
