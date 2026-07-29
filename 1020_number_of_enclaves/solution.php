<?php
// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numEnclaves($grid) {
        $m = count($grid);
        $n = count($grid[0]);

        $dfs = function ($r, $c) use (&$dfs, &$grid, $m, $n) {
            if ($r < 0 || $r >= $m || $c < 0 || $c >= $n || $grid[$r][$c] !== 1) {
                return;
            }
            $grid[$r][$c] = 0;
            $dfs($r + 1, $c);
            $dfs($r - 1, $c);
            $dfs($r, $c + 1);
            $dfs($r, $c - 1);
        };

        for ($i = 0; $i < $m; $i++) {
            $dfs($i, 0);
            $dfs($i, $n - 1);
        }
        for ($j = 0; $j < $n; $j++) {
            $dfs(0, $j);
            $dfs($m - 1, $j);
        }

        $ans = 0;
        foreach ($grid as $row) {
            foreach ($row as $cell) {
                $ans += $cell;
            }
        }
        return $ans;
    }
}
