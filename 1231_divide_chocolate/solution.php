<?php
// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

class Solution {
    /**
     * @param Integer[] $sweetness
     * @param Integer $k
     * @return Integer
     */
    function maximizeSweetness($sweetness, $k) {
        $lo = 1;
        $hi = intdiv(array_sum($sweetness), $k + 1);
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $pieces = 0;
            $current = 0;
            foreach ($sweetness as $value) {
                $current += $value;
                if ($current >= $mid) {
                    $pieces++;
                    $current = 0;
                }
            }
            if ($pieces >= $k + 1) $lo = $mid + 1;
            else $hi = $mid - 1;
        }
        return $hi;
    }
}
