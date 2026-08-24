<?php
// LeetCode 2774 - Array Upper Bound
// https://leetcode.com/problems/array-upper-bound/

class Solution {
    function upperBound($nums, $target) {
        $lo = 0;
        $hi = count($nums);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($nums[$mid] <= $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        if ($lo === 0 || $nums[$lo - 1] !== $target) return -1;
        return $lo - 1;
    }
}
