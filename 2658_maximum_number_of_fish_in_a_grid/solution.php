<?php
// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution {
    function findMaxFish($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dfs = function($r, $c) use (&$dfs, &$grid, $m, $n) {
            if ($r < 0 || $r >= $m || $c < 0 || $c >= $n || $grid[$r][$c] === 0) return 0;
            $fish = $grid[$r][$c];
            $grid[$r][$c] = 0;
            return $fish + $dfs($r + 1, $c) + $dfs($r - 1, $c) + $dfs($r, $c + 1) + $dfs($r, $c - 1);
        };
        $best = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] > 0) $best = max($best, $dfs($i, $j));
            }
        }
        return $best;
    }
}
