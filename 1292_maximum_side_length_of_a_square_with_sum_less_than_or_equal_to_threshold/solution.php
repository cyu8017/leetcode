<?php
// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution {
    /**
     * @param Integer[][] $mat
     * @param Integer $threshold
     * @return Integer
     */
    function maxSideLength($mat, $threshold) {
        $m = count($mat);
        $n = count($mat[0]);
        $prefix = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $prefix[$r + 1][$c + 1] = $mat[$r][$c] + $prefix[$r][$c + 1] + $prefix[$r + 1][$c] - $prefix[$r][$c];
            }
        }
        $possible = function ($size) use ($prefix, $m, $n, $threshold) {
            for ($r = $size; $r <= $m; $r++) {
                for ($c = $size; $c <= $n; $c++) {
                    $sum = $prefix[$r][$c] - $prefix[$r - $size][$c] - $prefix[$r][$c - $size] + $prefix[$r - $size][$c - $size];
                    if ($sum <= $threshold) return true;
                }
            }
            return false;
        };
        $lo = 0;
        $hi = min($m, $n);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($possible($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
