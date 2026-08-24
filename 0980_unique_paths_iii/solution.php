<?php
// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function uniquePathsIII($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $empty = 0;
        $sr = 0;
        $sc = 0;
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== -1) $empty++;
                if ($grid[$i][$j] === 1) { $sr = $i; $sc = $j; }
            }
        }
        $dfs = null;
        $dfs = function ($r, $c, $remain) use (&$dfs, &$grid, &$ans, $m, $n) {
            if ($grid[$r][$c] === 2) {
                if ($remain === 1) $ans++;
                return;
            }
            $temp = $grid[$r][$c];
            $grid[$r][$c] = -1;
            $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
            foreach ($dirs as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] !== -1)
                    $dfs($nr, $nc, $remain - 1);
            }
            $grid[$r][$c] = $temp;
        };
        $dfs($sr, $sc, $empty);
        return $ans;
    }
}
