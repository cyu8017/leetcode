<?php
// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution {
    /**
     * @param Integer[] $values
     * @return Integer
     */
    function minScoreTriangulation($values) {
        $n = count($values);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($len = 2; $len < $n; $len++) {
            for ($i = 0; $i + $len < $n; $i++) {
                $j = $i + $len;
                $best = PHP_INT_MAX;
                for ($k = $i + 1; $k < $j; $k++) {
                    $best = min($best, $dp[$i][$k] + $values[$i] * $values[$k] * $values[$j] + $dp[$k][$j]);
                }
                $dp[$i][$j] = $best;
            }
        }
        return $dp[0][$n - 1];
    }
}
