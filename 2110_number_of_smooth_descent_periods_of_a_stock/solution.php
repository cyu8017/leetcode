<?php
// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution {
    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function getDescentPeriods($prices) {
        $ans = 1;
        $cur = 1;
        $n = count($prices);
        for ($i = 1; $i < $n; $i++) {
            if ($prices[$i] === $prices[$i - 1] - 1) $cur++;
            else $cur = 1;
            $ans += $cur;
        }
        return $ans;
    }
}
