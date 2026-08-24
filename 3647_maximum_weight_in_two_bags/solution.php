<?php
// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

class Solution {
    function maxWeight($weights, $w1, $w2) {
        $f = [];
        for ($j = 0; $j <= $w1; $j++) $f[$j] = array_fill(0, $w2 + 1, 0);
        foreach ($weights as $x) {
            for ($j = $w1; $j >= 0; $j--) {
                for ($k = $w2; $k >= 0; $k--) {
                    if ($x <= $j) $f[$j][$k] = max($f[$j][$k], $f[$j - $x][$k] + $x);
                    if ($x <= $k) $f[$j][$k] = max($f[$j][$k], $f[$j][$k - $x] + $x);
                }
            }
        }
        return $f[$w1][$w2];
    }
}
