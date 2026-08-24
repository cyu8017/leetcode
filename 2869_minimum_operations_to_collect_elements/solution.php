<?php
// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution {
    function minOperations($nums, $k) {
        $need = [];
        for ($i = 1; $i <= $k; $i++) $need[$i] = true;
        $n = count($nums);
        for ($i = $n - 1; $i >= 0; $i--) {
            unset($need[$nums[$i]]);
            if (count($need) === 0) return $n - $i;
        }
        return $n;
    }
}
