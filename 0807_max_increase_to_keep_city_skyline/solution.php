<?php
// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxIncreaseKeepingSkyline($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $rowMax = array_fill(0, $m, 0);
        $colMax = array_fill(0, $n, 0);
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $rowMax[$r] = max($rowMax[$r], $grid[$r][$c]);
                $colMax[$c] = max($colMax[$c], $grid[$r][$c]);
            }
        }
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $ans += min($rowMax[$r], $colMax[$c]) - $grid[$r][$c];
            }
        }
        return $ans;
    }
}
