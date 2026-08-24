<?php
// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

class Solution {
    function last($nums) {
        $n = count($nums);
        if ($n === 0) return -1;
        return $nums[$n - 1];
    }
}
