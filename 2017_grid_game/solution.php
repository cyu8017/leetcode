<?php
// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function gridGame($grid) {
        $n = count($grid[0]);
        $top = 0;
        $bottom = 0;
        $ans = PHP_INT_MAX;
        foreach ($grid[0] as $v) $top += $v;
        for ($i = 0; $i < $n; $i++) {
            $top -= $grid[0][$i];
            $ans = min($ans, max($top, $bottom));
            $bottom += $grid[1][$i];
        }
        return $ans;
    }
}
