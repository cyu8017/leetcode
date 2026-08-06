<?php

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $cuts
     * @return Integer
     */
    function minCost($n, $cuts) {
        $points = array_merge([0], $cuts, [$n]);
        sort($points);
        $size = count($points);
        $dp = array_fill(0, $size, array_fill(0, $size, 0));
        for ($width = 2; $width < $size; $width++) {
            for ($left = 0; $left + $width < $size; $left++) {
                $right = $left + $width;
                $best = PHP_INT_MAX;
                for ($mid = $left + 1; $mid < $right; $mid++) {
                    $best = min($best, $dp[$left][$mid] + $dp[$mid][$right]);
                }
                if ($right > $left + 1) {
                    $best += $points[$right] - $points[$left];
                } else {
                    $best = 0;
                }
                $dp[$left][$right] = $best;
            }
        }
        return $dp[0][$size - 1];
    }
}
