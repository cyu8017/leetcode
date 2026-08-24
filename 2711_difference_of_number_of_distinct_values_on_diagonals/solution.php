<?php
// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution {
    function differenceOfDistinctValues($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = [];
        for ($i = 0; $i < $m; $i++) {
            $ans[$i] = array_fill(0, $n, 0);
            for ($j = 0; $j < $n; $j++) {
                $top = [];
                $bot = [];
                for ($r = $i - 1, $c = $j - 1; $r >= 0 && $c >= 0; $r--, $c--) $top[$grid[$r][$c]] = true;
                for ($r = $i + 1, $c = $j + 1; $r < $m && $c < $n; $r++, $c++) $bot[$grid[$r][$c]] = true;
                $ans[$i][$j] = abs(count($top) - count($bot));
            }
        }
        return $ans;
    }
}
