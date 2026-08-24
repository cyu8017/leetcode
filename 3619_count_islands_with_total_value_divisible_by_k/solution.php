<?php
// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

class Solution {
    function countIslands($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $dirs = [-1, 0, 1, 0, -1];
        $dfs = function($i, $j) use (&$grid, $m, $n, $dirs, &$dfs) {
            $s = $grid[$i][$j];
            $grid[$i][$j] = 0;
            for ($d = 0; $d < 4; $d++) {
                $x = $i + $dirs[$d];
                $y = $j + $dirs[$d + 1];
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n && $grid[$x][$y] > 0)
                    $s += $dfs($x, $y);
            }
            return $s;
        };
        $ans = 0;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] > 0 && $dfs($i, $j) % $k === 0) $ans++;
        return $ans;
    }
}
