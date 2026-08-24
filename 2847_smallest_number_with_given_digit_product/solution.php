<?php
// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

class Solution {
    function smallestNumber($n) {
        if ($n === 0) return '0';
        if ($n === 1) return '1';
        $digits = [];
        for ($d = 9; $d >= 2; $d--) {
            while ($n % $d === 0) {
                $digits[] = (string)$d;
                $n = intdiv($n, $d);
            }
        }
        if ($n > 1) return '-1';
        return implode('', array_reverse($digits));
    }
}
