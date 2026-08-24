<?php
// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution {
    function surfaceArea($grid) {
        $n = count($grid);
        $area = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== 0) {
                    $area += $grid[$i][$j] * 4 + 2;
                    if ($i > 0) $area -= min($grid[$i][$j], $grid[$i - 1][$j]) * 2;
                    if ($j > 0) $area -= min($grid[$i][$j], $grid[$i][$j - 1]) * 2;
                }
            }
        }
        return $area;
    }
}
