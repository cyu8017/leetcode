<?php
// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

class Solution {
    /**
     * @param Integer[] $ribbons
     * @param Integer $k
     * @return Integer
     */
    function maxLength($ribbons, $k) {
        $can = function ($length) use ($ribbons, $k) {
            $total = 0;
            foreach ($ribbons as $ribbon) {
                $total += intdiv($ribbon, $length);
            }
            return $total >= $k;
        };

        $lo = 1;
        $hi = max($ribbons);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($can($mid)) {
                $lo = $mid;
            } else {
                $hi = $mid - 1;
            }
        }
        return $can($lo) ? $lo : 0;
    }
}
