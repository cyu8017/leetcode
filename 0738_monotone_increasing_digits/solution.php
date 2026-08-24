<?php
// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

class Solution {
    function monotoneIncreasingDigits($n) {
        $digits = str_split((string)$n);
        $mark = count($digits);
        for ($i = count($digits) - 1; $i > 0; $i--) {
            if ($digits[$i] < $digits[$i - 1]) {
                $digits[$i - 1] = chr(ord($digits[$i - 1]) - 1);
                $mark = $i;
            }
        }
        for ($i = $mark; $i < count($digits); $i++) $digits[$i] = '9';
        return intval(implode('', $digits), 10);
    }
}
