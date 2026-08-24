<?php
// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

class Solution {
    function shortestBridge($grid) {
        $n = count($grid);
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $q = [];
        $dfs = function ($i, $j) use (&$dfs, &$grid, &$q, $n, $dirs) {
            if ($i < 0 || $j < 0 || $i >= $n || $j >= $n || $grid[$i][$j] !== 1) return;
            $grid[$i][$j] = 2;
            $q[] = [$i, $j];
            foreach ($dirs as [$di, $dj]) $dfs($i + $di, $j + $dj);
        };
        $found = false;
        for ($i = 0; $i < $n && !$found; $i++) {
            for ($j = 0; $j < $n && !$found; $j++) {
                if ($grid[$i][$j] === 1) {
                    $dfs($i, $j);
                    $found = true;
                }
            }
        }
        $steps = 0;
        while ($q) {
            $sz = count($q);
            for ($s = 0; $s < $sz; $s++) {
                [$i, $j] = array_shift($q);
                foreach ($dirs as [$di, $dj]) {
                    $ni = $i + $di;
                    $nj = $j + $dj;
                    if ($ni < 0 || $nj < 0 || $ni >= $n || $nj >= $n) continue;
                    if ($grid[$ni][$nj] === 1) return $steps;
                    if ($grid[$ni][$nj] === 0) {
                        $grid[$ni][$nj] = 2;
                        $q[] = [$ni, $nj];
                    }
                }
            }
            $steps++;
        }
        return -1;
    }
}
