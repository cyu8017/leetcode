<?php
// LeetCode 3912 - Valid Elements in an Array
// https://leetcode.com/problems/valid-elements-in-an-array/

class Solution {
    function findValidElements($nums) {
        $n = count($nums);
        $right = [];
        $right[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) $right[$i] = max($right[$i + 1], $nums[$i]);
        $left = 0;
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($x > $left || $i === $n - 1 || $x > $right[$i + 1]) $ans[] = $x;
            $left = max($left, $x);
        }
        return $ans;
    }
}
