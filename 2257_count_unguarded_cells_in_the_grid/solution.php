<?php
// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution {
    function countUnguarded($m, $n, $guards, $walls) {
        $grid = [];
        for ($i = 0; $i < $m; $i++) $grid[$i] = array_fill(0, $n, 0);
        foreach ($walls as $w) $grid[$w[0]][$w[1]] = 2;
        foreach ($guards as $g) $grid[$g[0]][$g[1]] = 2;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        foreach ($guards as $g) {
            foreach ($dirs as $d) {
                $r = $g[0] + $d[0];
                $c = $g[1] + $d[1];
                while ($r >= 0 && $r < $m && $c >= 0 && $c < $n && $grid[$r][$c] !== 2) {
                    $grid[$r][$c] = 1;
                    $r += $d[0];
                    $c += $d[1];
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] === 0) $ans++;
        return $ans;
    }
}
