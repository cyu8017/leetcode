<?php
// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution {
    function minimumArea($grid) {
        $x1 = count($grid);
        $y1 = count($grid[0]);
        $x2 = 0;
        $y2 = 0;
        for ($i = 0; $i < count($grid); $i++) {
            for ($j = 0; $j < count($grid[0]); $j++) {
                if ($grid[$i][$j] === 1) {
                    $x1 = min($x1, $i);
                    $y1 = min($y1, $j);
                    $x2 = max($x2, $i);
                    $y2 = max($y2, $j);
                }
            }
        }
        return ($x2 - $x1 + 1) * ($y2 - $y1 + 1);
    }
}
