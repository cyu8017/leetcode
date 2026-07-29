<?php
// LeetCode 1064 - Fixed Point
// https://leetcode.com/problems/fixed-point/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function fixedPoint($arr) {
        $lo = 0;
        $hi = count($arr) - 1;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] === $mid) {
                $ans = $mid;
                $hi = $mid - 1;
            } elseif ($arr[$mid] < $mid) {
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $ans;
    }
}
