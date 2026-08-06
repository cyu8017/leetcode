<?php
// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function sequentialDigits($low, $high) {
        $digits = '123456789';
        $answer = [];
        for ($length = 2; $length <= 9; $length++) {
            for ($start = 0; $start <= 9 - $length; $start++) {
                $value = (int)substr($digits, $start, $length);
                if ($value >= $low && $value <= $high) $answer[] = $value;
            }
        }
        return $answer;
    }
}
