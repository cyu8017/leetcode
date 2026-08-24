<?php
// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

class Solution {
    function splitArray($nums) {
        $n = count($nums);
        $s = array_fill(0, $n, 0);
        $f = array_fill(0, $n, true);
        $g = array_fill(0, $n, true);
        $s[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $s[$i] = $s[$i - 1] + $nums[$i];
            $f[$i] = $f[$i - 1];
            if ($nums[$i] <= $nums[$i - 1]) $f[$i] = false;
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            $g[$i] = $g[$i + 1];
            if ($nums[$i] <= $nums[$i + 1]) $g[$i] = false;
        }
        $inf = PHP_INT_MAX >> 2;
        $ans = $inf;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($f[$i] && $g[$i + 1]) {
                $s1 = $s[$i];
                $s2 = $s[$n - 1] - $s[$i];
                $ans = min($ans, abs($s1 - $s2));
            }
        }
        return $ans < $inf ? $ans : -1;
    }
}
