<?php
// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution {
    function findNonMinOrMax($nums) {
        if (count($nums) < 3) return -1;
        $a = $nums[0];
        $b = $nums[1];
        $c = $nums[2];
        return $a + $b + $c - max($a, $b, $c) - min($a, $b, $c);
    }
}
