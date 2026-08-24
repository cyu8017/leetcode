<?php
// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

class Solution {
    function sellingWood($m, $n, $prices) {
        $price = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        foreach ($prices as $p) $price[$p[0]][$p[1]] = $p[2];
        for ($h = 1; $h <= $m; ++$h) {
            for ($w = 1; $w <= $n; ++$w) {
                $best = $price[$h][$w];
                for ($i = 1; $i < $h; ++$i) $best = max($best, $dp[$i][$w] + $dp[$h - $i][$w]);
                for ($j = 1; $j < $w; ++$j) $best = max($best, $dp[$h][$j] + $dp[$h][$w - $j]);
                $dp[$h][$w] = $best;
            }
        }
        return $dp[$m][$n];
    }
}
