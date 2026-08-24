<?php
// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

class Solution {
    function minimumVisitedCells($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dist = [];
        for ($i = 0; $i < $m; $i++) $dist[] = array_fill(0, $n, -1);
        $q = [[0, 0]];
        $dist[0][0] = 1;
        while ($q) {
            $cur = array_shift($q);
            $r = $cur[0];
            $c = $cur[1];
            if ($r === $m - 1 && $c === $n - 1) return $dist[$r][$c];
            for ($nc = $c + 1; $nc <= $c + $grid[$r][$c] && $nc < $n; $nc++) {
                if ($dist[$r][$nc] === -1) {
                    $dist[$r][$nc] = $dist[$r][$c] + 1;
                    $q[] = [$r, $nc];
                }
            }
            for ($nr = $r + 1; $nr <= $r + $grid[$r][$c] && $nr < $m; $nr++) {
                if ($dist[$nr][$c] === -1) {
                    $dist[$nr][$c] = $dist[$r][$c] + 1;
                    $q[] = [$nr, $c];
                }
            }
        }
        return -1;
    }
}
