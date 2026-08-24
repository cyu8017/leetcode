<?php
// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

class Solution {
    function firstStableIndex($nums, $k) {
        $n = count($nums);
        $right = [];
        $right[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $right[$i] = min($right[$i + 1], $nums[$i]);
        $left = 0;
        for ($i = 0; $i < $n; $i++) {
            $left = max($left, $nums[$i]);
            if ($left - $right[$i] <= $k) return $i;
        }
        return -1;
    }
}
