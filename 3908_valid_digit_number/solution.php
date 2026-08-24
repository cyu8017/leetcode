<?php
// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

class Solution {
    function validDigit($n, $x) {
        $hasX = false;
        while ($n > 9) {
            $hasX = $hasX || ($n % 10 === $x);
            $n = intdiv($n, 10);
        }
        return $hasX && ($n !== $x);
    }
}
