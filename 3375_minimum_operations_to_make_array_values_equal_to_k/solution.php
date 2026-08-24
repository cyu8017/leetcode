<?php
// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

class Solution {
    function minOperations($nums, $k) {
        $seen = [];
        foreach ($nums as $x) {
            if ($x < $k) return -1;
            if ($x > $k) $seen[$x] = true;
        }
        return count($seen);
    }
}
