<?php
// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

class Solution {
    function reduce($nums, $fn, $init) {
        $acc = $init;
        foreach ($nums as $x) $acc = $fn($acc, $x);
        return $acc;
    }
}
