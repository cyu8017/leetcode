<?php
// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function getMaximumGold($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $dfs = function ($r, $c) use (&$dfs, &$grid, $rows, $cols) {
            $gold = $grid[$r][$c];
            $grid[$r][$c] = 0;
            $best = 0;
            foreach ([[1,0],[-1,0],[0,1],[0,-1]] as [$dr, $dc]) {
                $nr = $r + $dr; $nc = $c + $dc;
                if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && $grid[$nr][$nc]) {
                    $best = max($best, $dfs($nr, $nc));
                }
            }
            $grid[$r][$c] = $gold;
            return $gold + $best;
        };
        $ans = 0;
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($grid[$r][$c]) $ans = max($ans, $dfs($r, $c));
            }
        }
        return $ans;
    }
}
