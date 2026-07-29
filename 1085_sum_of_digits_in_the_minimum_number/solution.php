<?php
// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfDigits($nums) {
        $n = min($nums);
        $digitSum = 0;
        while ($n) {
            $digitSum += $n % 10;
            $n = intdiv($n, 10);
        }
        return $digitSum % 2 === 0 ? 1 : 0;
    }
}
