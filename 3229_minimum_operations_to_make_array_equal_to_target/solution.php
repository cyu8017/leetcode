<?php
// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

class Solution {
    function minimumOperations($nums, $target) {
        $f = abs($target[0] - $nums[0]);
        $n = count($target);
        for ($i = 1; $i < $n; $i++) {
            $x = $target[$i] - $nums[$i];
            $y = $target[$i - 1] - $nums[$i - 1];
            if ($x * $y > 0) {
                $d = abs($x) - abs($y);
                if ($d > 0) $f += $d;
            } else {
                $f += abs($x);
            }
        }
        return $f;
    }
}
