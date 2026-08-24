<?php
// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

class Solution {
    function maximumProfit($prices, $k) {
        $n = count($prices);
        $f = [];
        for ($i = 0; $i < $n; $i++) {
            $f[$i] = [];
            for ($j = 0; $j <= $k; $j++) $f[$i][$j] = [0, 0, 0];
        }
        for ($j = 1; $j <= $k; $j++) {
            $f[0][$j][1] = -$prices[0];
            $f[0][$j][2] = $prices[0];
        }
        for ($i = 1; $i < $n; $i++) {
            for ($j = 1; $j <= $k; $j++) {
                $f[$i][$j][0] = max($f[$i - 1][$j][0], max($f[$i - 1][$j][1] + $prices[$i], $f[$i - 1][$j][2] - $prices[$i]));
                $f[$i][$j][1] = max($f[$i - 1][$j][1], $f[$i - 1][$j - 1][0] - $prices[$i]);
                $f[$i][$j][2] = max($f[$i - 1][$j][2], $f[$i - 1][$j - 1][0] + $prices[$i]);
            }
        }
        return $f[$n - 1][$k][0];
    }
}
