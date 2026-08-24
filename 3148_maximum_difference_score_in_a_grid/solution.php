<?php
// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution {
    function maxScore($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $INF = 1 << 30;
        $f = [];
        for ($i = 0; $i < $m; $i++) $f[] = array_fill(0, $n, 0);
        $ans = -$INF;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $x = $grid[$i][$j];
                $mi = $INF;
                if ($i > 0) $mi = min($mi, $f[$i - 1][$j]);
                if ($j > 0) $mi = min($mi, $f[$i][$j - 1]);
                $ans = max($ans, $x - $mi);
                $f[$i][$j] = min($x, $mi);
            }
        }
        return $ans;
    }
}
