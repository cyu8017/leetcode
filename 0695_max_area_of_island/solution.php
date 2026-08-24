<?php
// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

class Solution {
    function maxAreaOfIsland($grid) {
        $dfs = function ($r, $c) use (&$dfs, &$grid) {
            if ($r < 0 || $r >= count($grid) || $c < 0 || $c >= count($grid[0]) || $grid[$r][$c] === 0) return 0;
            $grid[$r][$c] = 0;
            return 1 + $dfs($r + 1, $c) + $dfs($r - 1, $c) + $dfs($r, $c + 1) + $dfs($r, $c - 1);
        };
        $best = 0;
        for ($i = 0; $i < count($grid); $i++)
            for ($j = 0; $j < count($grid[0]); $j++)
                $best = max($best, $dfs($i, $j));
        return $best;
    }
}
