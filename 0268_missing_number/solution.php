<?php
// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function missingNumber($nums) {
        $length = count($nums);
        $expected = intdiv($length * ($length + 1), 2);
        $total = array_sum($nums);
        return $expected - $total;
    }
}
