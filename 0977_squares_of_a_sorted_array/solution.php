<?php
// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution {
    function sortedSquares($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $i = 0;
        $j = $n - 1;
        for ($k = $n - 1; $k >= 0; $k--) {
            if (abs($nums[$i]) > abs($nums[$j])) {
                $ans[$k] = $nums[$i] * $nums[$i];
                $i++;
            } else {
                $ans[$k] = $nums[$j] * $nums[$j];
                $j--;
            }
        }
        return $ans;
    }
}
