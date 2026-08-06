<?php
// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Boolean
     */
    function isMajorityElement($nums, $target) {
        $n = count($nums);
        $lo = 0; $hi = $n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($nums[$mid] < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        $left = $lo;
        $lo = 0; $hi = $n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($nums[$mid] <= $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo - $left > intdiv($n, 2);
    }
}
