<?php
// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

class Solution {
    function minFallingPathSum($matrix) {
        $n = count($matrix);
        $dp = $matrix[0];
        for ($i = 1; $i < $n; $i++) {
            $next = array_fill(0, $n, 0);
            for ($j = 0; $j < $n; $j++) {
                $best = $dp[$j];
                if ($j > 0) $best = min($best, $dp[$j - 1]);
                if ($j + 1 < $n) $best = min($best, $dp[$j + 1]);
                $next[$j] = $matrix[$i][$j] + $best;
            }
            $dp = $next;
        }
        return min($dp);
    }
}
