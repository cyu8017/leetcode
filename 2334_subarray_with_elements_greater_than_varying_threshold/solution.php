<?php
// LeetCode 2334 - Subarray With Elements Greater Than Varying Threshold
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

class Solution {
    function validSubarraySize($nums, $threshold) {
        $n = count($nums);
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($stack) > 0 && $nums[$stack[count($stack) - 1]] >= $nums[$i]) array_pop($stack);
            $left[$i] = count($stack) === 0 ? -1 : $stack[count($stack) - 1];
            $stack[] = $i;
        }
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($stack) > 0 && $nums[$stack[count($stack) - 1]] >= $nums[$i]) array_pop($stack);
            $right[$i] = count($stack) === 0 ? $n : $stack[count($stack) - 1];
            $stack[] = $i;
        }
        for ($i = 0; $i < $n; $i++) {
            $k = $right[$i] - $left[$i] - 1;
            if ($nums[$i] > intdiv($threshold, $k)) return $k;
        }
        return -1;
    }
}
