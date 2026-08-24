<?php
// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

class Solution {
    function numDistinctIslands($grid) {
        if ($grid === null || count($grid) === 0) return 0;
        $dfs = function ($r, $c, $br, $bc, &$path) use (&$dfs, &$grid) {
            if ($r < 0 || $r >= count($grid) || $c < 0 || $c >= count($grid[0]) || $grid[$r][$c] === 0) return;
            $grid[$r][$c] = 0;
            $path[] = ($r - $br) . ',' . ($c - $bc);
            $dfs($r + 1, $c, $br, $bc, $path);
            $dfs($r - 1, $c, $br, $bc, $path);
            $dfs($r, $c + 1, $br, $bc, $path);
            $dfs($r, $c - 1, $br, $bc, $path);
        };
        $shapes = [];
        for ($i = 0; $i < count($grid); $i++) {
            for ($j = 0; $j < count($grid[0]); $j++) {
                if ($grid[$i][$j] === 1) {
                    $path = [];
                    $dfs($i, $j, $i, $j, $path);
                    $shapes[implode(';', $path)] = true;
                }
            }
        }
        return count($shapes);
    }
}
