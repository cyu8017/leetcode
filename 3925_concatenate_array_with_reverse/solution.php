<?php
// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

class Solution {
    function concatWithReverse($nums) {
        $n = count($nums);
        $ans = array_fill(0, 2 * $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $ans[$i] = $nums[$i];
            $ans[$i + $n] = $nums[$n - $i - 1];
        }
        return $ans;
    }
}
