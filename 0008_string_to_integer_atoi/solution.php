<?php
// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function myAtoi($s) {
        $i = 0;
        $n = strlen($s);
        while ($i < $n && $s[$i] === ' ') {
            $i++;
        }
        if ($i >= $n) {
            return 0;
        }

        $sign = 1;
        if ($s[$i] === '-') {
            $sign = -1;
            $i++;
        } elseif ($s[$i] === '+') {
            $i++;
        }

        $result = 0;
        while ($i < $n && ctype_digit($s[$i])) {
            $digit = ord($s[$i]) - ord('0');
            if ($result > intdiv(PHP_INT_MAX - $digit, 10)) {
                return $sign === -1 ? PHP_INT_MIN : PHP_INT_MAX;
            }
            $result = $result * 10 + $digit;
            $i++;
        }

        return $sign * $result;
    }
}
