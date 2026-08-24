<?php
// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

class Solution {
    function minPathCost($grid, $moveCost) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = $grid[0];
        for ($r = 0; $r < $m - 1; ++$r) {
            $next = array_fill(0, $n, intdiv(2147483647, 2));
            for ($c = 0; $c < $n; ++$c) {
                $from = $grid[$r][$c];
                for ($nc = 0; $nc < $n; ++$nc) {
                    $next[$nc] = min($next[$nc], $dp[$c] + $moveCost[$from][$nc] + $grid[$r + 1][$nc]);
                }
            }
            $dp = $next;
        }
        $ans = $dp[0];
        for ($i = 1; $i < $n; $i++) $ans = min($ans, $dp[$i]);
        return $ans;
    }
}
