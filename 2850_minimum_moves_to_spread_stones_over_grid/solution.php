<?php
// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

class Solution {
    function minimumMoves($grid) {
        $extras = [];
        $zeros = [];
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                if ($grid[$i][$j] === 0) $zeros[] = [$i, $j];
                else if ($grid[$i][$j] > 1) {
                    for ($k = 0; $k < $grid[$i][$j] - 1; $k++) $extras[] = [$i, $j];
                }
            }
        }
        if (!count($zeros)) return 0;
        $best = 1 << 30;
        $dfs = function($i, $cost) use (&$dfs, &$extras, &$zeros, &$best) {
            if ($cost >= $best) return;
            if ($i === count($zeros)) {
                $best = $cost;
                return;
            }
            for ($j = 0; $j < count($extras); $j++) {
                if ($extras[$j][0] < 0) continue;
                $e = $extras[$j];
                $extras[$j] = [-1, $e[1]];
                $d = abs($e[0] - $zeros[$i][0]) + abs($e[1] - $zeros[$i][1]);
                $dfs($i + 1, $cost + $d);
                $extras[$j] = $e;
            }
        };
        $dfs(0, 0);
        return $best;
    }
}
