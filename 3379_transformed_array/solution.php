<?php
// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

class Solution {
    function constructTransformedArray($nums) {
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $j = (($i + $nums[$i]) % $n + $n) % $n;
            $ans[$i] = $nums[$j];
        }
        return $ans;
    }
}
