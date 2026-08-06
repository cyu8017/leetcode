<?php
// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maximumMinimumPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $heap = new SplMaxHeap();
        $heap->insert([$grid[0][0], 0, 0]);
        $seen = ['0,0' => true];
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (!$heap->isEmpty()) {
            [$val, $r, $c] = $heap->extract();
            if ($r === $m - 1 && $c === $n - 1) return $val;
            foreach ($dirs as [$dr, $dc]) {
                $nr = $r + $dr;
                $nc = $c + $dc;
                $key = "$nr,$nc";
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && !isset($seen[$key])) {
                    $seen[$key] = true;
                    $heap->insert([min($val, $grid[$nr][$nc]), $nr, $nc]);
                }
            }
        }
        return $grid[0][0];
    }
}
