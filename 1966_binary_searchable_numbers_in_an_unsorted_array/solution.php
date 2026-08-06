<?php
// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function binarySearchableNumbers($nums) {
        $n = count($nums);
        $ok = array_fill(0, $n, 1);
        $mx = PHP_INT_MIN;
        $mi = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] < $mx) {
                $ok[$i] = 0;
            } else {
                $mx = $nums[$i];
            }
        }
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($nums[$i] > $mi) {
                $ok[$i] = 0;
            } else {
                $mi = $nums[$i];
            }
        }
        return array_sum($ok);
    }
}
