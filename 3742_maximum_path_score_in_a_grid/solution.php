<?php
// LeetCode 3742 - Maximum Path Score in a Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

class Solution {
    function maxPathScore($grid, $k) {
        $INF = 1 << 30;
        $m = count($grid);
        $n = count($grid[0]);
        $f = [];
        for ($i = 0; $i < $m; $i++) {
            $f[$i] = [];
            for ($j = 0; $j < $n; $j++) $f[$i][$j] = array_fill(0, $k + 1, -1);
        }
        $dfs = function($i, $j, $kk) use (&$dfs, &$f, $grid, $INF) {
            if ($i < 0 || $j < 0 || $kk < 0) return -$INF;
            if ($i === 0 && $j === 0) return 0;
            if ($f[$i][$j][$kk] !== -1) return $f[$i][$j][$kk];
            $res = $grid[$i][$j];
            $nk = $kk;
            if ($grid[$i][$j] !== 0) $nk--;
            $a = $dfs($i - 1, $j, $nk);
            $b = $dfs($i, $j - 1, $nk);
            $res += max($a, $b);
            return $f[$i][$j][$kk] = $res;
        };
        $ans = $dfs($m - 1, $n - 1, $k);
        return $ans < 0 ? -1 : $ans;
    }
}
