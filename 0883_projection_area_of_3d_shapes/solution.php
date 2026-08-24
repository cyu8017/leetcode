<?php
// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution {
    function projectionArea($grid) {
        $n = count($grid);
        $top = 0;
        $front = 0;
        $side = 0;
        for ($i = 0; $i < $n; $i++) {
            $rowMax = 0;
            $colMax = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== 0) $top++;
                $rowMax = max($rowMax, $grid[$i][$j]);
                $colMax = max($colMax, $grid[$j][$i]);
            }
            $front += $rowMax;
            $side += $colMax;
        }
        return $top + $front + $side;
    }
}
