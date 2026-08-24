<?php
// LeetCode 0852 - Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function peakIndexInMountainArray($arr) {
        $lo = 0;
        $hi = count($arr) - 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] < $arr[$mid + 1]) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
