<?php
// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minFallingPathSum($grid) {
        $dp = $grid[0];
        $m = count($grid);
        $n = count($dp);
        for ($r = 1; $r < $m; $r++) {
            $first = 0;
            for ($i = 1; $i < $n; $i++) if ($dp[$i] < $dp[$first]) $first = $i;
            $secondValue = PHP_INT_MAX;
            for ($i = 0; $i < $n; $i++) {
                if ($i !== $first) $secondValue = min($secondValue, $dp[$i]);
            }
            if ($n === 1) $secondValue = 0;
            $nxt = [];
            for ($i = 0; $i < $n; $i++) {
                $nxt[$i] = $grid[$r][$i] + ($i === $first ? $secondValue : $dp[$first]);
            }
            $dp = $nxt;
        }
        return min($dp);
    }
}
