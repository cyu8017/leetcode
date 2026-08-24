<?php
// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

class Solution {
    function minimumRelativeLosses($prices, $queries) {
        sort($prices);
        $n = count($prices);
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $kk = $queries[$qi][0];
            $m = $queries[$qi][1];
            $losses = [];
            for ($i = 0; $i < $n; $i++) {
                if ($prices[$i] <= $kk) $losses[$i] = $prices[$i];
                else $losses[$i] = 2 * $kk - $prices[$i];
            }
            sort($losses);
            $sum = 0;
            for ($i = 0; $i < $m; $i++) $sum += $losses[$i];
            $ans[$qi] = $sum;
        }
        return $ans;
    }
}
