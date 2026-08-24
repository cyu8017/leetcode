<?php
// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution {
    function maxValueOfCoins($piles, $k) {
        $dp = array_fill(0, $k + 1, 0);
        foreach ($piles as $pile) {
            $ndp = $dp;
            $sum = 0;
            $plen = count($pile);
            for ($take = 1; $take <= $plen && $take <= $k; $take++) {
                $sum += $pile[$take - 1];
                for ($j = $take; $j <= $k; $j++)
                    $ndp[$j] = max($ndp[$j], $dp[$j - $take] + $sum);
            }
            $dp = $ndp;
        }
        return $dp[$k];
    }
}
